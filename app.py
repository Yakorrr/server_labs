from flask import Flask, jsonify
from flask_smorest import Api

from db import db
from resources.account import blp as AccountBlueprint
from resources.category import blp as CategoryBlueprint
from resources.record import blp as RecordBlueprint
from resources.user import blp as UserBlueprint

# defaultPage = Blueprint("index", __name__, description="Default page")
defaultPage = Flask(__name__)


def create_app():
    app = Flask(__name__)
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Finance REST API"
    app.config["API_VERSION"] = "v2.0"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    with app.app_context():
        db.create_all()

    api = Api(app)

    api.register_blueprint(UserBlueprint)
    api.register_blueprint(CategoryBlueprint)
    api.register_blueprint(RecordBlueprint)
    api.register_blueprint(AccountBlueprint)

    return app


@defaultPage.route("/")
def index():
    return jsonify("Welcome to the Flask App!")
