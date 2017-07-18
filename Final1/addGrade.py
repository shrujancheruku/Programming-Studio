from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
"""
Simple script to grade an assignment for a user
"""


def main():
    collection = MongoClient()["final1db"]["grades"]
    assign_collection = MongoClient()["final1db"]["assignments"]

    user_name = input("Enter the user name: ")
    assign_name = input("Enter the assignment name: ")
    assign_grade = input("Enter the assignment grade: ")

    try:
        collection.insert({"parent_user_id": user_name, "parent_assignment_id": assign_name, "grade": int(assign_grade)})
        print("Grade created.")
    except DuplicateKeyError:
        print("Grade already present in DB.")

    grade = collection.find_one({"parent_user_id": user_name, "parent_assignment_id": assign_name})
    assign_collection.find_one_and_update({'_id': assign_name}, {'$push': {'grade_id_list': grade.get('_id')}})

if __name__ == '__main__':
    main()