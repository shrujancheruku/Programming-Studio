from werkzeug.security import generate_password_hash
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
"""
Simple script to create a user, used for testing
"""


def main():
    # Connect to the DB
    collection = MongoClient()["final1db"]["users"]

    # Ask for data to store
    user = input("Enter your username: ")
    password = input("Enter your password: ")
    pass_hash = generate_password_hash(password, method='pbkdf2:sha256')

    # Insert the user in the DB
    try:
        collection.insert({"_id": user, "password": pass_hash, "class_id_list": []})
        print("User created.")
    except DuplicateKeyError:
        print("User already present in DB.")


if __name__ == '__main__':
    main()
