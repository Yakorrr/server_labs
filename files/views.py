from files.imports import *


CATEGORIES = []
USERS = []
RECORDS = []
RECORDS_RESULTS = {}


def create_user_data():
    return {"ID": uuid.uuid4().hex, "Username": names.get_first_name()}


def fill_users():
    for i in range(5): USERS.append(create_user_data())


def exists(array, element, default_key="ID"):
    """
    :param array: where we find
    :param element: what we find
    :param default_key: key we use
    :return: True if user or category exist
    """

    for i in array:
        try:
            if i.get(default_key) == element or element <= len(array): return True
        except TypeError: pass

    return False


def validate(request, obj):
    if obj not in request: return False

    return True


def get_array_string(array):
    return str(array).replace("'", '"')


def write_to_file(array, directory="logs", filename='', default_key="JSON"):
    path = os.path.join(os.getcwd(), directory)

    try:
        if not os.path.exists(path): os.mkdir(path)
    except FileNotFoundError: print('Cannot create file :(')
    finally:
        path = os.path.join(path, filename)
        result = json.loads(get_array_string(array))

        with open(path, 'w') as file:
            json.dump({default_key: result}, file, indent=4)


@app.route("/")
def index():
    return "Welcome to Flask App!"


@app.route("/categories")
def get_categories():
    default_key = "Categories"
    write_to_file(CATEGORIES, default_key=default_key, filename='categories.json')

    return jsonify({default_key: CATEGORIES})


@app.route("/category", methods=['POST'])
def create_category():
    request_categories_data = request.get_json()
    temp_name = ''

    if validate(request_categories_data, "Name"):
        temp_name = request_categories_data.get("Name")
    else: abort(404, message="Bad request: Category name not found!")

    if not exists(CATEGORIES, temp_name, default_key="Name"):
        CATEGORIES.append({"ID": len(CATEGORIES) + 1, "Name": temp_name})
    else: abort(400, message="This category is already exists.")

    return jsonify(request_categories_data)


@app.route("/users")
def get_users():
    default_key = "Users"
    write_to_file(USERS, default_key=default_key, filename='users.json')

    return jsonify({default_key: USERS})


@app.route("/user", methods=['POST'])
def create_user():
    request_user_data = request.get_json()
    temp_username = ''

    if validate(request_user_data, "Username"):
        temp_username = request_user_data.get("Username")
    else: abort(404, message="Bad request: Username not found!")

    if not exists(USERS, temp_username, default_key="Username"):
        USERS.append({"ID": create_user_data().get("ID"), "Username": temp_username})
    else: abort(400, message="This username is already used.")

    return jsonify(request_user_data)


@app.route("/records")
def get_records():
    default_key = "Records"
    write_to_file(RECORDS, default_key=default_key, filename='records.json')

    return jsonify({default_key: RECORDS})


@app.route("/record", methods=['POST'])
def create_record():
    request_record_data = request.get_json()
    keys = ["Username", "Category", "Amount"]
    temp_array = []
    temp_dict = {}

    for i in keys:
        if validate(request_record_data, i):
            temp = request_record_data.get(i)

            if i == "Category":
                for elem in CATEGORIES: temp = temp if elem.get("ID") != temp else elem.get("Name")

            temp_array.append(temp)
        else: abort(404, message="Bad request: %s not found!" % i)

    if not exists(USERS, temp_array[0], default_key="Username"):
        abort(404, message="This user doesn't exist.")
    elif not exists(CATEGORIES, temp_array[1], default_key="Name"):
        abort(404, message="This category doesn't exist.")
    else:
        for i in keys:
            temp_dict[i] = temp_array[keys.index(i)]
            if keys.index(i) == 1: temp_dict["Date"] = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")

        RECORDS.append(temp_dict)

    return jsonify(temp_dict)


@app.route("/user-records")
def show_user_records():
    return jsonify({"Users Records": RECORDS_RESULTS})


@app.route("/user-record")
def get_user_records():
    request_user_request = request.get_json()
    temp_username = ''
    temp_category = request_user_request.get("Category")

    if validate(request_user_request, "Username"):
        temp_username = request_user_request.get("Username")
    else: abort(404, message="Bad request: Username not found!")

    if not exists(USERS, temp_username, default_key="Username"):
        abort(404, message="This user doesn't exist.")

    if temp_category is not None and not exists(CATEGORIES, temp_category):
        abort(404, message="This category doesn't exist.")

    user_records_temp = []
    key = f'User %s' % temp_username + \
          (f', Category %s' % CATEGORIES[temp_category - 1].get("Name") if temp_category is not None else '')

    for i in RECORDS:
        if i.get("Username") == temp_username and \
                (temp_category is None or i.get("Category") == CATEGORIES[temp_category - 1].get("Name")):
            user_records_temp.append(i)

    RECORDS_RESULTS[key] = user_records_temp

    write_to_file(RECORDS_RESULTS, default_key='Users Records', filename='user-records.json')

    return jsonify({key: user_records_temp})


fill_users()
index()
