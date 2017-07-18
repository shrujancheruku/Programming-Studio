from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
"""
Simple script to add a user to a class, used for testing
"""


def main():
    collection = MongoClient()["final1db"]["classobjs"]

    user_name = input("Enter the user's name: ")
    class_name = input("Enter the class name: ")
    prof_name = input("Enter the professor name: ")

    try:
        collection.insert({"_id": class_name, "url": "#", 'professor_id': prof_name})
        print("Class created.")
    except DuplicateKeyError:
        print("Class already present in DB.")

    new_class = collection.find_one({"_id": class_name})
    user_collection = MongoClient()["final1db"]["users"]
    user_collection.find_one_and_update({'_id': user_name}, {'$push': {'class_id_list': new_class.get('_id')}})

if __name__ == '__main__':
    main()
