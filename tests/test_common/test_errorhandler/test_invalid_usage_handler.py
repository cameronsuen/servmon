"""Unit testing for servmon.common.errorhandler.invalid_usage_handler"""
from servmon import app
from servmon.common import invalid_usage
from servmon.common.errorhandler import invalid_usage_handler
import json
import pytest

@pytest.fixture
def app_mock():
    """Returns a mock of the application"""
    app.config['TESTING'] = True
    return app

@pytest.fixture
def invalid_usage_mock():
    """Returns an InvalidUsage object mock"""
    
    # Register the function to be tested as the error handler
    app.register_error_handler(invalid_usage.InvalidUsage, invalid_usage_handler.handle_invalid_usage)

    return invalid_usage.InvalidUsage('Test Message', 403, {'payload': 'test'})

@pytest.fixture
def invalid_usage_mock_estatus():
    """Returns an InvalidUsage object mock with invalid status code"""
    
    # Register the function to be tested as the error handler
    app.register_error_handler(invalid_usage.InvalidUsage, invalid_usage_handler.handle_invalid_usage)

    return invalid_usage.InvalidUsage('Test Message', 'Wrong status code', {'payload': 'test'})

@pytest.fixture
def invalid_usage_mock_epayload():
    """Returns an InvalidUsage object mock with invalid payload"""
    
    # Register the function to be tested as the error handler
    app.register_error_handler(invalid_usage.InvalidUsage, invalid_usage_handler.handle_invalid_usage)

    return invalid_usage.InvalidUsage('Test Message', 400, 'Wrong payload')

class TestInvalidUsageHandler(object):
    def test_invalid_usage_mock_estatus(self, app_mock, invalid_usage_mock_estatus):
        """Test handle_invalid_usage when passed with an object with wrong status"""
        
        @app.route('/test_invalid_usage_mock_estatus')
        def test_route_estatus():
            """Create a mock route that raises the InvalidUsage Exception"""
            raise invalid_usage_mock_estatus

        # Send a request to the mock route, asserting that a TypeError will be raised before it gets sent
        with app_mock.test_client() as client, pytest.raises(TypeError):
            res = client.get('/test_invalid_usage_mock_estatus')
    
    def test_invalid_usage_mock_epayload(self, invalid_usage_mock_epayload):
        """Test handle_invalid_usage when passed with an oject with wrong payload"""

        # Assert that the function raises ValueError
        with pytest.raises(ValueError):
            invalid_usage_handler.handle_invalid_usage(invalid_usage_mock_epayload)

    def test_invalid_usage_mock(self, app_mock, invalid_usage_mock):
        """Test handle_invalid_usage when passed with an working InvalidUsage"""

        @app.route('/test_invalid_usage_mock')
        def test_route():
            """Create a mock route that raises the InvalidUsage Exception"""
            raise invalid_usage_mock

        # Send a request to the mock route and checks the result
        with app_mock.test_client() as client:
            res = client.get('/test_invalid_usage_mock')
            assert json.loads(res.data) == {'message': 'Test Message', 'payload': 'test'}
