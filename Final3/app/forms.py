from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField, TextAreaField, SubmitField, FieldList, FormField
from wtforms.validators import DataRequired, ValidationError
"""
Form for reading in login and assignments
"""


def is_pdf():
    extensions = 'pdf'

    def _is_pdf(form, field):
        if not field.data or field.data.split('.')[-1] not in extensions:
            raise ValidationError("This is not a PDF file")
    return _is_pdf


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


class AssignmentForm(FlaskForm):
    submission = TextAreaField('Submission')
    file = FileField('FileSubmission')


class CreateAssignmentForm(FlaskForm):
    name = StringField('Assignment Name', validators=[DataRequired()])
    info = TextAreaField('Information')
    submit1 = SubmitField('submit')


class AddTAForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    submit2 = SubmitField('submit')


class JSONForm(FlaskForm):
    file = FileField('JSON', validators=[DataRequired()])
    submit3 = SubmitField('submit')


class SyllabusForm(FlaskForm):
    file = FileField('Syllabus', validators=[DataRequired()])
    submit4 = SubmitField('submit')


class AnnouncementForm(FlaskForm):
    text = TextAreaField('Announcement', validators=[DataRequired()])
    submit5 = SubmitField('submit')
