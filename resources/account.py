from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import IntegrityError

from db import db
from models import AccountModel
from schemas import AccountSchema

blp = Blueprint("account", __name__, description="Operations on account")


@blp.route("/account/<string:account_id>")
class Account(MethodView):
    @blp.response(200, AccountSchema)
    def get(self, account_id):
        return AccountModel.query.get_or_404(account_id)


@blp.route("/account")
class AccountList(MethodView):
    @blp.response(200, AccountSchema(many=True))
    def get(self):
        return AccountModel.query.all()

    @blp.arguments(AccountSchema)
    @blp.response(200, AccountSchema)
    def post(self, account_data):
        account = AccountModel(**account_data)

        try:
            db.session.add(account)
            db.session.commit()
        except IntegrityError:
            abort(400, message="Account for User %s already exists!" %
                               account_data.get("User_ID"))

        return account
