from files.imports import *
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

    @staticmethod
    def post():
        request_record_data = request.get_json()
        keys = ["Username", "Category", "Amount"]
        data = []
        record = {}

        for i in keys:
            if func.validate(request_record_data, i):
                data.append(request_record_data.get(i))
            else: abort(404, message="Bad request: %s not found!" % i)

        if not func.exists(USERS, data[0], default_key="Username"):
            abort(404, message="This user doesn't exist.")
        elif not func.exists(CATEGORIES, data[1], default_key="Name"):
            abort(404, message="This category doesn't exist.")
        else:
            record["ID"] = len(RECORDS) + 1
            for i in keys:
                record[i] = data[keys.index(i)]
                if keys.index(i) == 1: record["Date"] = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")

            RECORDS[str(uuid.uuid4().hex)] = record

        return record
