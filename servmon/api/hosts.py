"""Harddisk Module

This is the module responsible for getting the list of statuses of machines

"""

# jsonify is for constructing json response
# request is for getting request info (e.g. get parameters)
from flask import jsonify, request

# Import MongoDB support
from bson.son import SON
import pymongo

# This is a MUST for all APIs, import it to enable routing later
from servmon.api import api_blueprint
# Import common function you need, especially the errors that you would raise
# And the database connection module
from servmon.common import invalid_usage, db_connection
# Import error handlers
from servmon.common.errorhandler import invalid_usage_handler

import pprint

@api_blueprint.route('/hosts')
def get_hosts():
    """Get the hosts of machines"""
		
    # Initialize the database connection
    db = db_connection.get_db()
    # Get the required collection
    collection = db.machine_states

    # # Get the hosts
    # hosts = request.args.get('hosts') or ''

    projection = {
        '_id': False,
        # 'data.cpu': True,
        # 'data.ram': True,
        # 'data.process': True,
        # 'data.storage': True
    }

    pipeline = [
        { '$sort': SON([('hostname', -1), ('_id', 1)]) },
        { '$group': {
                '_id': '$hostname',
                'status': { '$first': '$status' },
                'ip': { '$first': '$ip' } 
            }
        },
        { '$project': {
                '_id': False,
                'status': True,
                'hostname': '$_id',
                'ip': True,
            }
        }
    ]

    print(pipeline)

    # Get the result from databas, excluding _id and seeded field
    # Sort the result by _id (document creation timestamp), get the latest one
    result = list(collection.aggregate(pipeline))

    # Nothing to return means wrong hostname
    if len(result) == 0:
        # error message, status code, OPTIONAL payload to illustrate error
        raise invalid_usage.InvalidUsage('No data found', 404,
                                         {'action': 'No mechine is found. Please check the connections.'})

    # Returns the result
    return jsonify(result)
