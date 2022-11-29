from files.imports import *
from files.schemas import *
import files.functions as func
from files.db import USERS, CATEGORIES, RECORDS

blp = Blueprint("record", __name__, description="Operations on record")


@blp.route("/record/<string:record_id>")
class Record(MethodView):
    @staticmethod
    def get(record_id):
        try:
            return RECORDS[record_id]
        except ValueError:
            abort(404, message="Record not found")


@blp.route("/record")
class RecordList(MethodView):
    @staticmethod
    def get():
        args = request.args.to_dict()
        username = args.get("Username")

        if not username:
            abort(400, "Bad request: Username needed")

        category_name = args.get("Category")

        if category_name:
            return func.get_records_by_filter(
                lambda x: (x["Username"] == username and x["Category"] == category_name)
            )

        func.write_to_file(list(RECORDS.values()), default_key="Records", filename='records.json')

        return func.get_records_by_filter(lambda x: x["Username"] == username)

    @blp.arguments(RecordSchema)
    def post(self, request_record_data):
        keys = ["Username", "Category", "Amount"]
        username = request_record_data.get("Username")
        category = request_record_data.get("Category")
        record = {}

        if not func.exists(USERS, username, default_key="Username"):
            abort(404, message="This user doesn't exist.")
        elif not func.exists(CATEGORIES, category, default_key="Name"):
            abort(404, message="This category doesn't exist.")
        else:
            record = {
                "ID": len(RECORDS) + 1,
                **request_record_data,
                "Date": datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
            }

            RECORDS[str(uuid.uuid4().hex)] = record

        return record
