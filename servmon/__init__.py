from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

# Import the Blueprint object as blueprint
from servmon.api import api_blueprint as api_blueprint
# Import the actual APIs, has to be imported BEFORE blueprint registration
from servmon.api import *

# Register the blueprint, APIs accessable at /api/*
app.register_blueprint(api_blueprint, url_prefix='/api')

