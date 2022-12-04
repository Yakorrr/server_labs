import json
import os
from db import RECORDS


def exists(array, element):
    return element in array


def get_array_string(array):
    return str(array).replace("'", '"')


def write_to_file(array, directory="logs", filename='', default_key="JSON"):
    path = os.path.join(os.getcwd(), directory)

    try:
        if not os.path.exists(path): os.mkdir(path)
    except FileNotFoundError:
        print('Cannot create file :(')
    finally:
        path = os.path.join(path, filename)
        result = json.loads(get_array_string(array))

        with open(path, 'w') as file:
            json.dump({default_key: result}, file, indent=4)


def get_records_by_filter(filter_function):
    return list(filter(filter_function, RECORDS.values()))
