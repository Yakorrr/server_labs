from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy import update, create_engine
from sqlalchemy.exc import IntegrityError

from db import *
from models import RecordModel, AccountModel
from schemas import RecordSchema, RecordQuerySchema

blp = Blueprint("record", __name__, description="Operations on record")


@blp.route("/record/<string:record_id>")
class Record(MethodView):
    @blp.response(200, RecordSchema)
    def get(self, record_id):
        return RecordModel.query.get_or_404(record_id)


@blp.route("/record")
class RecordList(MethodView):
    @blp.arguments(RecordQuerySchema, location="query", as_kwargs=True)
    @blp.response(200, RecordSchema(many=True))
    def get(self, **kwargs):
        user_id = kwargs.get("User_ID")

        if not user_id:
            abort(400, "Bad request: Username needed")

        query = RecordModel.query.filter(RecordModel.User_ID == user_id)

        category_id = kwargs.get("Category_ID")

        if category_id:
            query = query.filter(RecordModel.Category_ID == category_id)

        return query.all()

    @blp.arguments(RecordSchema)
    @blp.response(200, RecordSchema)
    def post(self, record_data):
        record = RecordModel(**record_data)
        user_id = record_data.get("User_ID")

        engine = create_engine("sqlite:///data.db")

        try:
            db.session.add(record)

            connection = engine.connect()
            upd = AccountModel.update() \
                .values({AccountModel.Balance: AccountModel.Balance -
                        RecordModel.query.with_entities(RecordModel.Amount)
                        .filter(RecordModel.User_ID == user_id)}) \
                .where(AccountModel.User_ID == user_id)
            # print(str(upd))
            connection.execute(upd)

            db.session.commit()
        except IntegrityError:
            abort(400, message="Ooops, creating record went wrong!")

        return record
