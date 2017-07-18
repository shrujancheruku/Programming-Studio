from werkzeug.security import check_password_hash
"""
Schemas for the database.
"""


class User:

    def __init__(self, username):
        self.username = username

    username = ""
    class_id_list = []
    is_professor = False
    is_TA = False
    grade_id_list = []

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.username

    @staticmethod
    def validate_login(password_hash, password):
        return check_password_hash(password_hash, password)


class ClassObj:

    name = ""
    professor_id = ""
    url = ""
    student_id_list = []
    assignment_id_list = []
    ta_list = []


class Assignment:

    parent_class_id = ""
    grade_id = ""


class Grade:

    parent_user_id = ""
    parent_assignment = ""
    grade = 0
