
================
Package Metadata
================

- **author:** Caitlin Kavenaugh

- **classifier**:: 

    Intended Audience :: Science/Research
    Topic :: Scientific/Engineering

- **description-file:** README.txt

- **entry_points**:: 

    [openmdao.surrogatemodel]
    neural_net.neural_net.NeuralNet=neural_net.neural_net:NeuralNet
    [openmdao.component]
    test_neural_net.Sin=test_neural_net:Sin
    test_neural_net.Simulation=test_neural_net:Simulation
    NN_sin.Simulation=NN_sin:Simulation
    NN_sin.Sin=NN_sin:Sin
    [openmdao.container]
    test_neural_net.Sin=test_neural_net:Sin
    test_neural_net.Simulation=test_neural_net:Simulation
    neural_net.neural_net.NeuralNet=neural_net.neural_net:NeuralNet
    NN_sin.Simulation=NN_sin:Simulation
    NN_sin.Sin=NN_sin:Sin

- **home-page:** https://github.com/OpenMDAO-Plugins/neural_net

- **keywords:** openmdao

- **license:** GNU General Public License, version 2

- **maintainer:** Kenneth T. Moore

- **maintainer-email:** kenneth-t-mooore-1@nasa.gov

- **name:** neural_net

- **project-url:** https://github.com/OpenMDAO-Plugins/NeuralNet-Plugin

- **requires-dist**:: 

    openmdao.main
    ffnet

- **requires-python**:: 

    >=2.6
    <3.0

- **static_path:** [ '_static' ]

- **summary:** OpenMDAO wrapper for a Feedforward Neural Net surrogate model that can be slotted into the MetaModel component

- **version:** 0.7

