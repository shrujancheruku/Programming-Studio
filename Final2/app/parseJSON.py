import json


def get_students(class_json):
    data = json.load(class_json)
    return data['students']
