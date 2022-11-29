from files.imports import *
import files.functions as func
from files.db import CATEGORIES

blp = Blueprint("category", __name__, description="Operations on category")


@blp.route("/category/<string:category_name>")
class Category(MethodView):
    @staticmethod
    def get(category_name):
        try:
            return CATEGORIES[category_name]
        except ValueError:
            abort(404, message="Category not found")


@blp.route("/category")
class CategoryList(MethodView):
    @staticmethod
    def get():
        func.write_to_file(list(CATEGORIES.values()), default_key="Categories", filename='categories.json')

        return list(CATEGORIES.values())

    @staticmethod
    def post():
        request_categories_data = request.get_json()
        category = {}
        name = ''

        if func.validate(request_categories_data, "Name"):
            name = request_categories_data.get("Name")
        else:
            abort(404, message="Bad request: Category name not found!")

        if not func.exists(CATEGORIES, name, default_key="Name"):
            category = {"ID": len(CATEGORIES) + 1, "Name": name}
            CATEGORIES[name] = category
        else:
            abort(400, message="This category is already exists.")

        return category
