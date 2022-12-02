import json
import os
import uuid
from datetime import datetime

from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort, Api
from marshmallow import Schema, fields
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

from files.resources.user import blp as UserBlueprint
from files.resources.category import blp as CategoryBlueprint
from files.resources.record import blp as RecordBlueprint

from db import *
from functions import *
from schemas import *

from files import app
