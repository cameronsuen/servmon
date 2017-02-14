"""Db Module

This module provides the functionality to connect to the MongoDB Database
For more information, please check out
http://flask.pocoo.org/docs/0.12/appcontext/#creating-an-application-context
"""

from flask import g
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

from servmon import app


def get_db():
    client = getattr(g, '_mongo_client', None)
    if client is None:
        client = connect_to_client()
        # TODO: Change db name to environmental variable
        db = client['test_database']

    return db


@app.teardown_appcontext
def teardown_db(exception):
    client = getattr(g, '_mongo_client', None)
    if client is not None:
        client.close()


def connect_to_client():
    client = MongoClient()
    try:
        # Fire a cheap, simple command to check if client is working
        client.admin.command('ismaster')
    except ConnectionFailure:
        # Prints an error message in case MongoClient connection fails
        # TODO: Add robus error message and actions
        print('Server Not Available')

    return client
