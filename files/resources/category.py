from files.imports import uuid, Blueprint, MethodView, CategorySchema, write_to_file, CATEGORIES


blp = Blueprint("category", __name__, description="Operations on category")


@blp.route("/category/<string:category_name>")
class Category(MethodView):
    @blp.response(200, CategorySchema)
    def get(self, category_id):
        return CATEGORIES[category_id]


@blp.route("/category")
class CategoryList(MethodView):
    @blp.response(200, CategorySchema(many=True))
    def get(self):
        write_to_file(list(CATEGORIES.values()), default_key="Categories", filename='categories.json')

        return list(CATEGORIES.values())

    @blp.arguments(CategorySchema)
    @blp.response(200, CategorySchema)
    def post(self, request_categories_data):
        category_id = uuid.uuid4().hex

        category = {
            "ID": category_id,
            **request_categories_data
        }

        CATEGORIES[category_id] = category

        return category
