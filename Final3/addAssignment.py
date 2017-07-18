from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
"""
Simple script to add a an assignment to a class, used for testing
"""


def main():
    collection = MongoClient()["final2db"]["assignments"]
    class_collection = MongoClient()["final2db"]["classobjs"]

    class_name = input("Enter the class name: ")
    assign_name = input("Enter the assignment name: ")
    my_class = class_collection.find_one({"_id": class_name})

    try:
        collection.insert({"name": assign_name, 'parent_class_id': my_class.get('_id'), 'grade_id_list': []})
        print("Assignment created.")
    except DuplicateKeyError:
        print("Assignment already present in DB.")

    assign = collection.find_one({"name": assign_name})
    class_collection.find_one_and_update({'_id': class_name}, {'$push': {'assignment_id_list': assign.get('_id')}})

if __name__ == '__main__':
    main()
