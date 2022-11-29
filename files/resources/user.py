from files.imports import *
import files.views as view
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
        view.write_to_file(USERS, default_key="Users", filename='users.json')

        return list(USERS.values())

    @staticmethod
    def post():
        request_user_data = request.get_json()
        user = {}
        username = ''

        if view.validate(request_user_data, "Username"):
            username = request_user_data.get("Username")
        else: abort(404, message="Bad request: Username not found!")

        if not view.exists(USERS, username, default_key="Username"):
            user = {"ID": uuid.uuid4().hex, "Username": username}
            USERS[username] = user
        else: abort(400, message="This username is already used.")

        return user