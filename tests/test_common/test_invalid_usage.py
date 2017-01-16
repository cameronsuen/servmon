"""Testing for invalid_usage module in common package"""

from servmon.common import invalid_usage
import pytest

# A pytest.fixture defines a function that returns an object/result repeatable 
# for testing
# It is useful for providing a basic test object without having to create one 
# in every test case
@pytest.fixture
def invalid_usage_without_optional():
    """Returns InvalidUsage without optional parameters (message only)"""
    return invalid_usage.InvalidUsage('test invalid usage without optional')


@pytest.fixture
def invalid_usage_with_optional():
    """Returns InvalidUsage with all parameters (message, status_code and payload"""
    return invalid_usage.InvalidUsage('test invalid usage with optional', 300, {'payload': 'test'})

class TestInvalidUsage(object):
    """Unit tests for InvalidUsage classes"""
    def test_init_without_optional(self, invalid_usage_without_optional):
        """Test the constructor options without passing in the optional parameters""" 
        assert invalid_usage_without_optional.message == 'test invalid usage without optional'
        assert invalid_usage_without_optional.status_code == 400 
        assert invalid_usage_without_optional.payload is None

    def test_unit_with_optional(self, invalid_usage_with_optional):
        """Test the constructor options without passing in the optional parameters"""
        assert invalid_usage_with_optional.message == 'test invalid usage with optional'
        assert invalid_usage_with_optional.status_code == 300
        assert invalid_usage_with_optional.payload == {'payload': 'test'}

    def test_to_dict_without_payload(self, invalid_usage_without_optional):
        """Test the to_dict function with an exception without payload"""
        assert invalid_usage_without_optional.to_dict() == {'message': 'test invalid usage without optional'}
    
    def test_to_dict_with_payload(self, invalid_usage_with_optional):
        """Test the to_dict function with an exception with payload"""
        assert invalid_usage_with_optional.to_dict() == {'payload': 'test', 'message': 'test invalid usage with optional'}
