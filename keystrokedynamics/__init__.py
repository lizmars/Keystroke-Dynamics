from flask import Flask
from flask.ext.navigation import Navigation
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
nav = Navigation(app)
from keystrokedynamics import keystroke
