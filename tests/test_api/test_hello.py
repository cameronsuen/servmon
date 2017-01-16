"""Unit testing of servmon.api.hello module

This is the unit testing of the sevmon.api.hello module
This file serves as a sample of API unit testing 
Please pay attention to how this is implemented
"""

from datetime import date
from servmon import app
from servmon.api import hello
import json
import pytest

# A fixtue is simply function that returns object that you need for unit testing 
@pytest.fixture
def app_mock():
    """Enables Testing flag and returns the app"""
    app.config['Testing'] = True
    return app

class TestHello(object):
    """Please use a class to wrap all the test cases of a particular api

    Note that to accomdate Google's Style Guide, a class should extend object if
    it has no subclasses
    """
    def test_hello_without_name(self, app_mock):
        """ Test hello without supplying name in query string
        Define a test case in a function, note that every class method has self as
        the first parameter.
        We also inject the fixture app_mock into the test case for use below
        """

        # Call /api/hello using test client, storing the response in res 
        res = app_mock.test_client().get('/api/hello')

        # Assert that the status code returned is 400
        assert res.status_code == 400
        
        # Assert that the response should be a json token as below
        assert json.loads(res.data) == {'message': 'No name specified', 'action': 'Please specify a name in query string'}


    def test_hello_with_name(self, app_mock):
        """ Test hello with a supplied name in query string"""

        # Call /api/hello?name=test using test client, storing the response in res
        res = app_mock.test_client().get('/api/hello?name=test')

        # Assert that the status code returned is 200
        assert res.status_code == 200

        # Assert that the response should be a json token as below
        assert json.loads(res.data) == {'name': 'test', 'date': date.today().strftime('%Y-%m-%d')}
