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
    collection = db.localhost_states

    # Set up the data
    sample_machine_state = {
        'seeded': True,
        'used': 200,
        'total': 1000,
        'partitions': [{'filesystem': '/dev/sda1', 'mountpoint': '/',
                        'used': 100, 'subtotal': 500},
                       {'filesystem': '/dev/sda2', 'mountpoint': '/var',
                        'used': 100, 'subtotal': 500}]
    }

    # Actual insertion of data
    collection.insert_one(sample_machine_state)


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
