from files.imports import uuid, Blueprint, MethodView, UserSchema, write_to_file, USERS


blp = Blueprint("user", __name__, description="Operations on user")


@blp.route("/user/<string:username>")
class User(MethodView):
    @blp.response(200, UserSchema)
    def get(self, user_id):
        return USERS[user_id]

    @blp.response(200, UserSchema)
    def delete(self, user_id):
        deleted_user = USERS[user_id]
        del USERS[user_id]

        return deleted_user


@blp.route("/user")
class UserList(MethodView):
    @blp.response(200, UserSchema(many=True))
    def get(self):
        write_to_file(list(USERS.values()), default_key="Users", filename='users.json')

        return list(USERS.values())

    @blp.arguments(UserSchema)
    @blp.response(200, UserSchema)
    def post(self, request_user_data):
        user_id = uuid.uuid4().hex

        user = {
            "ID": user_id,
            **request_user_data
        }

        USERS[user_id] = user

        return user
