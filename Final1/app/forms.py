from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField, TextAreaField
from wtforms.validators import DataRequired
"""
Form for reading in login and assignments
"""


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


class AssignmentForm(FlaskForm):
    submission = TextAreaField('Submission')
    file = FileField('FileSubmission')