from pymongo import MongoClient

WTF_CSRF_ENABLED = True
SECRET_KEY = 'my-secret-key'
DB_NAME = 'final2db'

DATABASE = MongoClient()[DB_NAME]
CLASS_COLLECTION = DATABASE.classobjs
USERS_COLLECTION = DATABASE.users
ASSIGNMENT_COLLECTION = DATABASE.assignments
GRADE_COLLECTION = DATABASE.grades

GOOGLE_LOGIN_CLIENT_ID = "1042364314422-kj34kfv0v98h0mi4s5pg9jncbojg7pia.apps.googleusercontent.com"
GOOGLE_LOGIN_CLIENT_SECRET = "T6ug9qjKOD0a9tvOXwqlF3qO"

OAUTH_CREDENTIALS = {
        'google': {
            'id': GOOGLE_LOGIN_CLIENT_ID,
            'secret': GOOGLE_LOGIN_CLIENT_SECRET
        }
}

DEBUG = True
