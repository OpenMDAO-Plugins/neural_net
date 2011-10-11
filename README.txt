
This OpenMDAO plugin contains the wrapper for a Feedforward Neural Net
surrogate model that can be slotted into the MetaModel component. The
calculations are carried out using the external package ffnet (Feed-forward
neural network for python) developed by Marek Wojciechowski under the GPL
license. More information about this package can be found here:

http://ffnet.sourceforge.net/

Installing this plugin should auotmatically install ffnet if it is able to. We
have built binary distributions of ffnet for Windows (Python 2.6 and 2.7) and
are hosting them at openmdao.org to make installation easier. (Note, binaries
built from ffnet version 0.7, released 09/09/2011.

To view the Sphinx documentation for this distribution, type:

plugin_docs neural_net

