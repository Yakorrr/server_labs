import json
import os
import uuid
from datetime import datetime

from flask import jsonify, request
from flask.views import MethodView
from flask_smorest import Blueprint, abort, Api

from files import app