from flask import jsonify 
from http import HTTPStatus

class InvalidUsage(Exception):
    """
    An exception class to handle invalid usage of the APIs
    """
    def __init__(self, message, status=400, payload=None):
        """Constructor for the exception class
    
        :param message: a human readable error message
        :type message: str
        :param status: the HTTP status implied (not return code of command)
        :type status: int or 400
        :param payload: an optional payload to fully illustrate the error
        :type payload: iterable or None
        """

        Exception.__init__(self)
        self.message = message
        self.status_code = status
        self.payload = payload

    def to_dict(self):
        """Converts exception to Python dictionary (to be serialized as JSON)
        
        :rtype: dict
        """

        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv
