from werkzeug.security import check_password_hash
"""
Schemas for the database.
"""


class User:
    def __init__(self, username):
        self._id = username
        self.is_professor = False
        self.is_TA = False
        self.class_id_list = []

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self._id

    @staticmethod
    def validate_login(password_hash, password):
        return check_password_hash(password_hash, password)


class ClassObj:
    def __init__(self, name):
        self._id = name
        self.professor_id = ""
        self.student_id_list = []
        self.assignment_id_list = []
        self.ta_list = []


class Assignment:
    def __init__(self, name):
        self.name = name
        self.parent_class_id = ""
        self.grade_id_list = []
        self.info = ""


class Grade:
    def __init__(self, grade):
        self.parent_user_id = ""
        self.parent_assignment_id = ""
        self.grade = grade
        self.submission = ""
        self.submission_file = None
