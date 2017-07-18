import json
"""
The JSON Handler class
This class takes in the json and returns the nested dicts
"""


def parse_json(data):
    with open(data) as json_file:
        data = json.load(json_file)
        return data
