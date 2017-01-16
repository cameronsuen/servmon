"""Sample module

This is just a sample module to illustrate how to create and use an API module
Please check the source code to see how to write the documentation (in docstring)

"""

#jsonify is for constructing json response
#request is for getting request info (e.g. get parameters)
from flask import jsonify, request

# This is a MUST for all APIs, import it to enable routing later
from servmon.api import api_blueprint
# Import common function you need, especially the errors that you would raise
from servmon.common import invalid_usage, today 
# Import error handlers
from servmon.common.errorhandler import invalid_usage_handler

@api_blueprint.route('/hello')
def hello():
    """ A test function returning hello world
    
        :query string name: a name to display
        :>jsonarr string name: a name to display, not present when error occurs
        :>jsonarr string date: today's date, not present when error occurs
        :>jsonarr string message: error message, present when error occurs 
        :>jsonarr string action: how to correct error, present when error occurs

        :status 200: returns a token of name and date
        :status 400: returns an error token
    """

    name = request.args.get('name') or None
    if name == None:
        # error message, status code, OPTIONAL payload to illustrate error
        raise invalid_usage.InvalidUsage('No name specified', 400, {'action': 'Please specify a name in query string'}) 

    token = {'name': request.args.get('name'), 'date': today.today().strftime('%Y-%m-%d')}
    return jsonify(token)
