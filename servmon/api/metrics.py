"""Harddisk Module

This is the module responsible for exposing hard disk statuses

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

@api_blueprint.route('/metrics')
def get_metrics():
    """Get the metrics of machines

        **Example request**:

        .. sourcecode:: http

            GET /api/metrics?hostname=localhost&detailMetric=harddisk&detailMetric=cpu&detailMetric=ram&detailMetric=process
            Host: localhost:5000
            Accept: application/json

        **Example response**:

        .. sourcecode:: http

           HTTP/1.0 200 OK
           Content-Type: application/json

           {
             "hostname": "localhost",
             "status": true,
             data: {
               "CPU": "20%",
               "CPUData": {
                 cores: [{
                   "name": "Core 1",
                   "usage": "20%",
                   "frequency": "100000MHz"
                 }, {
                   "name": "Core 2",
                   "usage": "20%",
                   "frequency": "1000000MHz"
                 }]
               },
               "storage": "80%",
               "storageData": {
                 "storagePartitions": [{
                   name: "Partition",
                   filesystem: "/dev/sda1",
                   mountPt: "/",
                   storage: "600GB/1000GB"
                 }]
               },
               "RAM": "65%",
               "RAMData" {
                 "totalMemory": "3.90GB/16.00GB",
                 "buffers": "9GB",
                 "swapUsage": "1GB/16GB"
               },
               "process": true,
               "processData": {
                 "processes": [{
                   name: "Process A",
                   status: false,
                   PID: "123456",
                   UIDs: "0(root)/1(daemon)",
                   GUIDs: "3(user)/3(sys)",
                   CPUOccupied: "15%",
                   RAMOccupied: "900MB/7%"
                 }]
               }
             }
           }

        :type post_id: string
        :reqheader Accept: application/json
        :resheader Content-Type: application/json
        :status 200: ok, returns a token of name and date
        :status 404: hostname not found, returns an error token
    """

    # Initialize the database connection
    db = db_connection.get_db()
    # Get the required collection
    collection = db.machine_states

    # Get the hostname
    hostname = request.args.get('hostname') or ''

    # Get all query parameters as a MultiDict
    all_args = request.args.getlist('detailMetric')

    pid = request.args.get('pid') or ''

    projection = {
        '_id': False,
        'data.cpu': True,
        'data.ram': True,
        'data.process': True,
        'data.storage': True
    }

    pipeline = [
        { '$sort': SON([('hostname', -1), ('_id', 1)]) },
        { '$group': {
                '_id': '$hostname',
                'status': { '$first': '$status' },
                'data': { '$first': '$data' } 
            }
        },
        { '$project': {
                '_id': False,
                'status': True,
                'hostname': '$_id',
                'data.cpu': True,
                'data.ram': True,
                'data.process': True,
                'data.storage': True
            }
        }
    ]

    for metric in all_args:
        pipeline[2]['$project']['data.' + metric + 'Data'] = True

    if 'data.processData' not in pipeline[2]['$project']:
        pipeline[2]['$project']['data.processData.processes.status'] =  True
        pipeline[2]['$project']['data.processData.processes.name'] = True
        pipeline[2]['$project']['data.processData.processes.pid'] = True

    if hostname != '':
        pipeline.insert(0, { '$match': { 'hostname': hostname } })
        if pid != '':
            pipeline.insert(1, {'$unwind': '$data.processData.processes'})
            pipeline.insert(2, {'$match': {'data.processData.processes.pid': pid}})
    print(pipeline)

    # Get the result from databas, excluding _id and seeded field
    # Sort the result by _id (document creation timestamp), get the latest one
    result = list(collection.aggregate(pipeline))

    # Nothing to return means wrong hostname
    if len(result) == 0:
        # error message, status code, OPTIONAL payload to illustrate error
        raise invalid_usage.InvalidUsage('No data found', 404,
                                         {'action': 'Please specify correct hostname, '})

    # Returns the result
    return jsonify(result)

