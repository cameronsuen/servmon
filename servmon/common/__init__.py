"""Package that contains common utilties to be used by all APIs

This is a package where common utilties like common functions, exception classes
and handlers are found.  

Note that to use the common utilities, they must be imported individually in 
each module (file)

e.g. `from servmon.common import today` (assuming that all APIs 
will be placed in the api subfolder) 

You can import all common functions by calling `from servmon.common import *`, though 
this is not encouraged in general

"""

from flask import jsonify
from os.path import dirname, basename, isfile
import glob

# Find paths of all .py files under current directory
modules = glob.glob(dirname(__file__)+'/*.py')
# Extract module names and put them in __all__ array
# so that from api import * imports all modules
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) ]
