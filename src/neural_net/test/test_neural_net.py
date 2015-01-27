import unittest

from numpy import sin
import numpy.random as numpy_random

from openmdao.main.api import Assembly, Component, SequentialWorkflow, set_as_top

from openmdao.lib.datatypes.api import Float
from openmdao.lib.drivers.api import DOEdriver
from openmdao.lib.doegenerators.api import FullFactorial, Uniform
from openmdao.lib.components.api import MetaModel

from neural_net.neural_net import NeuralNet


class Sin(Component):

    x = Float(0, iotype="in", units="rad", low=0, high=20)

    f_x = Float(0.0, iotype="out")

    def execute(self):
        self.f_x = .5*sin(self.x)


class Simulation(Assembly):

    def __init__(self):
        super(Simulation, self).__init__()

        #Components
        self.add("sin_calc", Sin())
        self.add("sin_verify", Sin())
        self.add("sin_meta_model", MetaModel(params=('x',),
                                             responses=('f_x',)))
        self.sin_meta_model.default_surrogate = NeuralNet(n_hidden_nodes=5)

        #Training the MetaModel
        self.add("DOE_Trainer", DOEdriver())
        self.DOE_Trainer.DOEgenerator = FullFactorial()
        # Seems to need a lot of training data for decent prediction of sin(x),
        # at least with default 'cg' method.
        self.DOE_Trainer.DOEgenerator.num_levels = 2500
        self.DOE_Trainer.add_parameter("sin_calc.x", low=0, high=20)
        self.DOE_Trainer.add_response("sin_calc.f_x")

        self.connect('DOE_Trainer.case_inputs.sin_calc.x',
                     'sin_meta_model.params.x')
        self.connect('DOE_Trainer.case_outputs.sin_calc.f_x',
                     'sin_meta_model.responses.f_x')

        #MetaModel Validation
        self.add("DOE_Validate", DOEdriver())
        self.DOE_Validate.DOEgenerator = Uniform()
        self.DOE_Validate.DOEgenerator.num_samples = 100
        self.DOE_Validate.add_parameter(("sin_meta_model.x", "sin_verify.x"),
                                        low=0, high=20)
        self.DOE_Validate.add_response("sin_verify.f_x")
        self.DOE_Validate.add_response("sin_meta_model.f_x")

        #Iteration Hierarchy
        self.driver.workflow.add(['DOE_Trainer', 'DOE_Validate'])
        self.DOE_Trainer.workflow.add('sin_calc')
        self.DOE_Validate.workflow.add(('sin_verify', 'sin_meta_model'))


class NeuralNetTestCase(unittest.TestCase):

    def setUp(self):
        numpy_random.seed(10)

    def test_training(self):
        sim = set_as_top(Simulation())
        sim.run()

        #This is how you can access any of the data
        train_inputs = sim.DOE_Trainer.case_inputs.sin_calc.x
        train_actual = sim.DOE_Trainer.case_outputs.sin_calc.f_x
        inputs = sim.DOE_Validate.case_inputs.sin_meta_model.x
        actual = sim.DOE_Validate.case_outputs.sin_verify.f_x
        predicted = sim.DOE_Validate.case_outputs.sin_meta_model.f_x

        avg_error = sum([abs(p-a) for a, p in zip(actual, predicted)])/len(actual)

#        print
#        for a, p in zip(actual, predicted):
#            print 'predicted, actual, error', p, a, p-a
#        print 'average error', avg_error
#
#        import pylab
#        pylab.scatter(train_inputs, train_actual, c='g', label='training data')
#        pylab.scatter(inputs, predicted, c='b', label='predicted result')
#        pylab.scatter(inputs, actual, c='r', label='correct result')
#        pylab.legend()
#        pylab.show()

        self.assertTrue(avg_error <= .08)


if __name__ == "__main__":
    unittest.main()

