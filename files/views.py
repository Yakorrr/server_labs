from files.imports import *

CATEGORIES = []
USERS = []
RECORDS = []
GET_RECORDS_RESULTS = {}


def create_user_data():
    def count_digits(number):
        digits = 0

        if number == 0: return 1
        while number > 0:
            number //= 10
            digits += 1

        return digits

    temp = math.floor(random.random() * 1e6)
    user_id = temp if temp >= 1e5 else temp * int(1e6 // 10 ** count_digits(temp))
    user_name = names.get_first_name()

    return {"ID": user_id, "Name": user_name}


def fill_users():
    for i in range(5):
        temp_user = create_user_data()

        while USERS.count(temp_user.get("ID")) > 0: temp_user = create_user_data()

        USERS.append(temp_user)


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


def get_array_string(array):
    return str(array).replace("'", '"')


def create_date(date_string):
    formats = ["%d/%m/%Y", "%d %b %Y", "%d %B %Y"]
    time_format = '%H:%M:%S'

    date = re.sub(r'[-\n.]', "/", date_string)
    time = datetime.now().strftime(time_format) if date.count(" ") % 2 == 0 else ''

    for i in formats:
        try:
            return str(datetime.strptime(date + (" " + time if len(time) != 0 else time),
                                         i + " " + time_format))
        except ValueError: pass

    raise ValueError()


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
    temp_name = request_categories_data.get("Name")

    if not exists(CATEGORIES, temp_name, default_key="Name"):
        CATEGORIES.append(dict({"ID": len(CATEGORIES) + 1, "Name": temp_name}))
    else: return jsonify("This category is already exists.")

    return jsonify(request_categories_data)


@app.route("/users")
def get_users():
    default_key = "Users"
    write_to_file(USERS, default_key=default_key)

    return jsonify({default_key: USERS})


@app.route("/user", methods=['POST'])
def create_user():
    request_user_data = request.get_json()
    temp_id = create_user_data().get("ID")

    # Check if created id is free. If not -> new id
    while exists(USERS, temp_id): temp_id = create_user_data().get("ID")

    USERS.append({"ID": int(temp_id), "Name": request_user_data.get("Name")})

    return jsonify(request_user_data)


@app.route("/records")
def get_records():
    default_key = "Records"
    write_to_file(RECORDS, default_key=default_key)

    return jsonify({default_key: RECORDS})


@app.route("/record", methods=['POST'])
def create_record():
    request_record_data = request.get_json()

    # 'User ID' and 'Category Name' must be greater than 0
    if request_record_data.get("ID_User") <= 0:
        return jsonify("User ID must be greater than zero!")
    elif request_record_data.get("ID_Category") <= 0:
        return jsonify("Category ID must be greater than zero!")
    else:
        # If user doesn't exist -> not found
        if not exists(USERS, request_record_data.get("ID_User"), default_key="Name"):
            return jsonify("This user doesn't exist.")
        # If category doesn't exist -> not found
        elif not exists(CATEGORIES, request_record_data.get("ID_Category")):
            return jsonify("This category doesn't exist.")
        else:
            try:
                temp_dict = {"User ID": USERS[request_record_data.get("ID_User") - 1].get("ID"),
                             "Category Name": CATEGORIES[request_record_data.get("ID_Category") - 1].get("Name"),
                             "Date": create_date(request_record_data.get("Date")),
                             "Amount": request_record_data.get("Amount")}
                RECORDS.append(temp_dict)
            except ValueError: return jsonify("Unsupported date format. Please try again.")

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
