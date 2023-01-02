from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import IntegrityError, NoResultFound

from db import db
from models import AccountModel, UserModel
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
        user_id = account_data.get("user_id")

        try:
            user = UserModel.query.filter(UserModel.id == user_id).one()

            db.session.add(user)
            db.session.add(account)
            db.session.commit()
        except NoResultFound:
            abort(404, message="User not found")
        except IntegrityError:
            db.session.rollback()

            account = AccountModel.query.filter(AccountModel.user_id == user_id).one()
            account.balance += account_data.get("balance")

            db.session.add(account)
            db.session.commit()
        finally:
            return account
