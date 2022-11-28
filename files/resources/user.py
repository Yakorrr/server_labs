from files.imports import *
import files.views as view
from files.db import USERS

blp = Blueprint("user", __name__, description="Operations on user")

@blp.route("/user/<string:user_id>")
class User(MethodView):
    @staticmethod
    def get(user_id):
        try:
            return USERS[user_id]
        except ValueError:
            abort(404, message="User not found")

    @staticmethod
    def delete(user_id):
        try:
            temp_user = USERS[user_id]
            del USERS[user_id]

            return temp_user
        except KeyError:
            abort(404, message="User not found")

@blp.route("/user")
class UserList(MethodView):
    @staticmethod
    def get():
        default_key = "Users"
        view.write_to_file(USERS, default_key=default_key, filename='users.json')

        return {default_key: USERS}

    @staticmethod
    def post():
        request_user_data = request.get_json()
        temp_user = {}
        temp_username = ''

        if view.validate(request_user_data, "Username"):
            temp_username = request_user_data.get("Username")
        else: abort(404, message="Bad request: Username not found!")

        if not view.exists(USERS, temp_username, default_key="Username"):
            temp_user = {"ID": uuid.uuid4().hex, "Username": temp_username}
            USERS.append(temp_user)
        else: abort(400, message="This username is already used.")

        return jsonify(temp_user)