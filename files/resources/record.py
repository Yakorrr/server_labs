from files.imports import *
from files.schemas import *
import files.functions as func
from files.db import USERS, CATEGORIES, RECORDS

blp = Blueprint("record", __name__, description="Operations on record")


@blp.route("/record/<string:record_id>")
class Record(MethodView):
    @blp.response(200, RecordSchema)
    def get(self, record_id):
        try:
            return RECORDS[record_id]
        except ValueError:
            abort(404, message="Record not found")


@blp.route("/record")
class RecordList(MethodView):
    @blp.arguments(RecordQuery, location="query", as_kwargs=True)
    @blp.response(200, RecordSchema(many=True))
    def get(self, **kwargs):
        username = kwargs.get("Username")

        if not username:
            abort(400, "Bad request: Username needed")

        category_name = kwargs.get("Category")

        if category_name:
            return func.get_records_by_filter(
                lambda x: (x["Username"] == username and x["Category"] == category_name)
            )

        func.write_to_file(list(RECORDS.values()), default_key="Records", filename='records.json')

        return func.get_records_by_filter(lambda x: x["Username"] == username)

    @blp.arguments(RecordSchema)
    @blp.response(200, RecordSchema)
    def post(self, request_record_data):
        if not func.exists(USERS, request_record_data["Username"], default_key="Username"):
            abort(404, message="This user doesn't exist.")
        if not func.exists(CATEGORIES, request_record_data["Category"], default_key="Name"):
            abort(404, message="This category doesn't exist.")

        record_id = uuid.uuid4().hex

        record = {
            "ID": record_id,
            **request_record_data,
            "Date": datetime.now().strftime("%Y-%m-%d, %H:%M:%S"),
        }

        RECORDS[record_id] = record

        return record
