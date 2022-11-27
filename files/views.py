from files.imports import *


CATEGORIES = []
USERS = []
RECORDS = []
GET_RECORDS_RESULTS = {}


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
    def get_list_name():
        return [i for i, j in globals().items() if j == array][0].lower()

    # default file extension - .json
    if filename == '': filename = get_list_name() + ".json"

    path = os.path.join(os.getcwd(), directory)

    try:
        if not os.path.exists(path): os.mkdir(path)
    except FileNotFoundError: print('Cannot create file :(')
    finally:
        temp_elements = array if array != GET_RECORDS_RESULTS \
            else get_array_string(GET_RECORDS_RESULTS)

        path = os.path.join(path, filename)
        result = json.loads(get_array_string(temp_elements))

        with open(path, 'w') as file:
            json.dump({default_key: result}, file, indent=4)


@app.route("/")
def index():
    return "Welcome to Flask App!"


@app.route("/categories")
def get_categories():
    default_key = "Categories"
    write_to_file(CATEGORIES, default_key=default_key)

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
    write_to_file(USERS, default_key=default_key)

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
    write_to_file(RECORDS, default_key=default_key)

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
                for elem in CATEGORIES:
                    temp = temp if elem.get("ID") != temp or elem.get("Name") != temp else elem.get("Name")

            temp_array.append(temp)
        else: abort(404, message="Bad request: %s not found!" % i)

    if not exists(USERS, temp_array[0], default_key="Username"):
        abort(404, message="This user doesn't exist.")
    elif not exists(CATEGORIES, temp_array[1], default_key="Name"):
        abort(404, message="This category doesn't exist.")
    else:
        for i in keys:
            temp_dict[i] = temp_array[keys.index(i)]
            if keys.index(i) == 1: temp_dict["Date"] = datetime.now()

        RECORDS.append(temp_dict)

    return jsonify(temp_dict)


@app.route("/user-records")
def show_user_records():
    return jsonify({"Users Records": GET_RECORDS_RESULTS})


@app.route("/user-record")
def get_user_records():
    request_user_id = request.get_json()
    user_number = request_user_id.get("User")
    id_category = request_user_id.get("Category")
    category_name = ''

    if not exists(USERS, user_number):
        return jsonify("This user doesn't exist.")
    else: user_id = USERS[user_number - 1].get("ID")

    if id_category is not None:
        if not exists(CATEGORIES, id_category):
            return jsonify("This category doesn't exist.")
        else: category_name = CATEGORIES[id_category - 1].get("Name")
    else: pass

    user_records_temp = []
    key = f'User %s' % user_id + \
          (f', Category %s' % category_name if category_name != '' else '')

    for i in RECORDS:
        if i.get("User ID") == user_id and \
                (category_name == '' or i.get("Category Name") == category_name):
            user_records_temp.append(i)

    GET_RECORDS_RESULTS[key] = user_records_temp

    write_to_file(GET_RECORDS_RESULTS, default_key='Users Records', filename='user-records.json')

    return jsonify({key: user_records_temp})


fill_users()
index()
