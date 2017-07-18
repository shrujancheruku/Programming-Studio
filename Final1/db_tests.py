from pymongo import MongoClient
from werkzeug.security import generate_password_hash
import unittest
"""
Tests for the database schemas
"""

class DBTest(unittest.TestCase):

    def setUp(self):
        user_collection = MongoClient()["final1db"]["users"]
        user_collection.insert({"_id": 'test_user', 'class_id_list': [],
                                "password": generate_password_hash('123456', method='pbkdf2:sha256')})
        class_collection = MongoClient()["final1db"]["classobjs"]
        class_collection.insert({"_id": "CS 242", 'student_id_list': []})
        test_user = user_collection.find_one({"_id": 'test_user'})
        test_class = class_collection.find_one({"_id": "CS 242"})
        user_collection.update_one({'_id': 'test_user'}, {'$push': {'class_id_list': test_class.get('_id')}})
        class_collection.update_one({'_id': 'CS 242'}, {'$push': {'student_id_list': test_user.get('_id')}})

    def test_userval(self):
        user_collection2 = MongoClient()["final1db"]["users"]
        class_collection2 = MongoClient()["final1db"]["classobjs"]
        test_user2 = user_collection2.find_one({"_id": 'test_user'})
        test_class2 = class_collection2.find_one({"_id": "CS 242"})
        self.assertTrue(test_user2.get('_id') == 'test_user')
        self.assertTrue(test_class2.get('_id') in test_user2['class_id_list'])
        self.assertTrue(test_class2.get('_id') == 'CS 242')
        self.assertTrue(test_user2.get('_id') in test_class2['student_id_list'])

    # def test_classval(self):
    #     user_collection = MongoClient()["final1db"]["users"]
    #     class_collection = MongoClient()["final1db"]["classobjs"]
    #     test_user = user_collection.find_one({"_id": 'test_user'})
    #     test_class = class_collection.find_one({"_id": "CS 242"})
    #     self.assertTrue(test_class.get('_id') == 'CS 242')
    #     self.assertTrue(test_user.get('_id') in test_user.get('student_id_list'))


if __name__ == '__main__':
    unittest.main()
