from files.imports import *
from files.schemas import *
import files.functions as func
from files.db import USERS

blp = Blueprint("user", __name__, description="Operations on user")


@blp.route("/user/<string:username>")
class User(MethodView):
    @staticmethod
    def get(username):
        try:
            return USERS[username]
        except ValueError:
            abort(404, message="User not found")

    @staticmethod
    def delete(user_id):
        try:
            deleted_user = USERS[user_id]
            del USERS[user_id]

            return deleted_user
        except KeyError:
            abort(404, message="User not found")


@blp.route("/user")
class UserList(MethodView):
    @staticmethod
    def get():
        func.write_to_file(list(USERS.values()), default_key="Users", filename='users.json')

        return list(USERS.values())

    @blp.arguments(UserSchema)
    def post(self, request_user_data):
        user = {}
        username = request_user_data.get("Username")

        if not func.exists(USERS, username, default_key="Username"):
            user = {"ID": uuid.uuid4().hex, "Username": username}
            USERS[username] = user
        else: abort(400, message="This username is already used.")

        return user
