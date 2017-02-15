"""Harddisk Module

This is the module responsible for exposing hard disk statuses

"""

# jsonify is for constructing json response
# request is for getting request info (e.g. get parameters)
from flask import jsonify, request

# Import MongoDB support
import pymongo

# This is a MUST for all APIs, import it to enable routing later
from servmon.api import api_blueprint
# Import common function you need, especially the errors that you would raise
# And the database connection module
from servmon.common import invalid_usage, db_connection
# Import error handlers
from servmon.common.errorhandler import invalid_usage_handler


@api_blueprint.route('/<hostname>/harddisk')
def show_harddisk_usage(hostname):
    """ Get the latest harddisk usage of a machine with particular `hostname`

        **Example request**
        .. sourcecode:: http

           GET /localhost/harddisk
           Host: localhost:5000
           Accept: application/json

        **Example response**
        .. sourcecode:: http

           HTTP/1.0 200 OK
           Content-Type: application/json

           {
             "metric": "harddisk",
             "partitions": [
               {
                 "filesystem": "/dev/sda1",
                 "mountpoint": "/",
                 "subtotal": 500,
                 "used": 100
               },
               {
                 "filesystem": "/dev/sda2",
                 "mountpoint": "/var",
                 "subtotal": 500,
                 "used": 100
               }
              ]
            }
        "
        :param hostname: hostname of the machine
        :type post_id: string
        :reqheader Accept: application/json
        :resheader Content-Type: application/json
        :status 200: ok, returns a token of name and date
        :status 404: hostname not found, returns an error token
    """

    # Initialize the database connection
    db = db_connection.get_db()
    # Get the required collection
    collection = db[hostname + '_states']

    # Get the result from databas, excluding _id and seeded field
    # Sort the result by _id (document creation timestamp), get the latest one
    result = collection.find(projection={'_id': False, 'seeded': False}).limit(1).sort('_id', pymongo.DESCENDING)

    # Nothing to return means wrong hostname
    if result.count() == 0:
        # error message, status code, OPTIONAL payload to illustrate error
        raise invalid_usage.InvalidUsage('Hostname Not Found', 404,
                                         {'action': 'Please specify a correct hostname'})

    # Returns the result
    return jsonify(result[0])
