"""
This is the package containing all the public APIs
"""

from flask import Blueprint
from os.path import dirname, basename, isfile
import glob

api_blueprint = Blueprint('api', __name__)

# Find paths of all .py files under current directory
modules = glob.glob(dirname(__file__)+'/*.py')
# Extract module names and put them in __all__ array
# so that from api import * imports all modules
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) ]
