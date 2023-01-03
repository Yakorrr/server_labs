from flask.views import MethodView
from flask_jwt_extended import create_access_token, jwt_required
from flask_smorest import Blueprint, abort
from passlib.handlers.pbkdf2 import pbkdf2_sha256
from sqlalchemy.exc import IntegrityError, NoResultFound

from db import db
from models import UserModel
from schemas import UserSchema

blp = Blueprint("user", __name__, description="Operations on user")


@blp.route("/user/<string:username>")
class User(MethodView):
    @jwt_required()
    @blp.response(200, UserSchema)
    def get(self, user_id):
        return UserModel.query.get_or_404(user_id)

    @jwt_required()
    @blp.response(200, UserSchema)
    def delete(self, user_id):
        raise NotImplementedError("Not implemented now")


@blp.route("/user")
class UserList(MethodView):
    @jwt_required()
    @blp.response(200, UserSchema(many=True))
    def get(self):
        return UserModel.query.all()


@blp.route("/auth/register")
class AuthUser(MethodView):
    @blp.arguments(UserSchema)
    @blp.response(200, UserSchema)
    def post(self, user_data):
        user = UserModel(
            username=user_data["username"],
            password=pbkdf2_sha256.hash(user_data["password"]),
        )

        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            abort(400, message="This username is already used")

        return user


@blp.route("/auth/login")
class LoginUser(MethodView):
    @blp.arguments(UserSchema)
    @blp.response(200, UserSchema)
    def post(self, login_data):
        user = UserModel(**login_data)
        login_username = login_data.get("username")
        access_token = None

        try:
            login_user = UserModel.query.filter(UserModel.username == login_username).one()

            if login_user and pbkdf2_sha256.verify(login_data["password"], login_user.password):
                access_token = create_access_token(identity=user.id)
        except NoResultFound:
            abort(404, message="User not found")
        except IntegrityError:
            abort(400, message="Bad request. Please try again")

        return access_token
