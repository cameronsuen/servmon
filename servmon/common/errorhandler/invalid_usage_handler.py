"""This module defines handlers for InvalidUsage exceptions defined in common package

Note that to use the error handlers, you must import them 
"""

from flask import jsonify 
from servmon.api import api_blueprint
from servmon.common import invalid_usage 

@api_blueprint.errorhandler(invalid_usage.InvalidUsage)
def handle_invalid_usage(error):
    """Return JSON response upon InvalidUsage exception 
       
    :param error: the exception object raised
    :type error: InvalidUsage
    :rtype: json
    """
    
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

