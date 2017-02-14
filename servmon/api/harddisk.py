"""Harddisk Module

This is the module responsible for exposing hard disk statuses

"""

# jsonify is for constructing json response
# request is for getting request info (e.g. get parameters)
from flask import jsonify, request

# Import MongoDB support
import pymongo
from bson.json_util import dumps

# This is a MUST for all APIs, import it to enable routing later
from servmon.api import api_blueprint
# Import common function you need, especially the errors that you would raise
# And the database connection module
from servmon.common import invalid_usage, db_connection
# Import error handlers
from servmon.common.errorhandler import invalid_usage_handler


@api_blueprint.route('/<hostname>/harddisk')
def show_harddisk_usage(hostname):
    """

        :string hostname: hostname of the machine
        :>jsonarr string name: a name to display, not present when error occurs
        :>jsonarr string date: today's date, not present when error occurs
        :>jsonarr string message: error message, present when error occurs
        :>jsonarr string action: how to correct error, present when error occurs

        :status 200: returns a token of name and date
        :status 400: returns an error token
    """

    # Initialize the database connection
    db = db_connection.get_db()
    # Get the required collection
    collection = db[hostname + '_states']

    result = collection.find().limit(1).sort('_id', pymongo.DESCENDING)

    if result.count() == 0:
        # error message, status code, OPTIONAL payload to illustrate error
        raise invalid_usage.InvalidUsage('Hostname Not Found', 404,
                                         {'action': 'Please specify a correct hostname'})

    # Returns the result
    return dumps(result[0])
