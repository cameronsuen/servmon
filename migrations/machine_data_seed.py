""" A Seed File to seed the Mongo DB with Test Data """

# Import pymongo module to allow operations on mongo
from pymongo import MongoClient


def up():
    """ Seed the database with test data """

    # Mandatory for every mongodb call
    client = MongoClient()
    # Select which database to use
    db = client.test_database
    # Select which collection to use, each collection stores data of one machine
    collection = db.machine_states

    # Remove the old collection
    collection.remove({})

    sample_machine_states = list()

    # Set up the data
    sample_machine_states.append({
        'hostname': 'localhost',
        'status': True,
        'data': {
            'cpu': '20%',
            'cpuData': {
                'cores': [{
                    'name': 'Core 1',
                    'usage': '20%',
                    'frequency': '2000MHz',
                },
                {
                    'name': 'Core 2',
                    'usage': '30%',
                    'frequency': '2000MHz'
                }]
            },
            'storage': '80%',
            'storageData': {
                'storagePartitions': [{
                    'name': 'Partition',
                    'filesystem': '/dev/sda1',
                    'mountPt': '/',
                    'storage': '600GB/1000GB'
                }]
            },
            'ram': '65%',
            'ramData': {
                'totalMemory': '3.90GB/16.00GB',
                'buffers': '9GB',
                'swapUsage': '1GB/16GB'
            },
            'process': True,
            'processData': {
                'processes': [{
                    'name': 'Process A',
                    'status': True,
                    'PID': 123456,
                    'UID': '0(root)/1(daemon)',
                    'GUID': '3(user)/3(sys)',
                    'CPUOccupeid': '15%',
                    'RAMOccupied': '900MB/7%'
                }]
            }

        },
        'seeded': True
    })

    sample_machine_states.append({
        'hostname': 'sample-domain',
        'status': True,
        'data': {
            'cpu': '20%',
            'cpuData': {
                'cores': [{
                    'name': 'Core 1',
                    'usage': '40%',
                    'frequency': '2000MHz',
                },
                {
                    'name': 'Core 2',
                    'usage': '50%',
                    'frequency': '2000MHz'
                }]
            },
            'storage': '80%',
            'storageData': {
                'storagePartitions': [{
                    'name': 'Partition',
                    'filesystem': '/dev/sda1',
                    'mountPt': '/',
                    'storage': '600GB/1000GB'
                }]
            },
            'ram': '65%',
            'ramData': {
                'totalMemory': '3.90GB/16.00GB',
                'buffers': '9GB',
                'swapUsage': '1GB/16GB'
            },
            'process': True,
            'processData': {
                'processes': [{
                    'name': 'Process A',
                    'status': True,
                    'PID': 123456,
                    'UID': '0(root)/1(daemon)',
                    'GUID': '3(user)/3(sys)',
                    'CPUOccupeid': '15%',
                    'RAMOccupied': '900MB/7%'
                }]
            }

        },
        'seeded': True
    })

    # Actual insertion of data
    collection.insert_many(sample_machine_states);


def down():
    """ Remove the seeded test data """

    # Mandatory for every mongodb call
    client = MongoClient()
    # Select which database to use
    db = client.test_database
    # Select which collection to use, each collection stores data of one machine
    collection = db.localhost_states

    # Remove the data having attribute seeded = True
    collection.delete_many({'seeded': True})
