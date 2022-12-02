from files.imports import app, Api, UserBlueprint, CategoryBlueprint, RecordBlueprint


app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Finance REST API"
app.config["API_VERSION"] = "v1.1.0"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)
api.register_blueprint(UserBlueprint)
api.register_blueprint(CategoryBlueprint)
api.register_blueprint(RecordBlueprint)


@app.route("/")
def index():
    return "Welcome to Flask App!"
