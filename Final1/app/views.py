from app import app, lm
from flask import request, redirect, render_template, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from .forms import LoginForm, AssignmentForm
from .models import User
from .auth import OAuthSignIn
from datetime import datetime
"""
Views for the Flask app. Contains the routes for the page routing
"""


@login_required
@app.route('/')
def home():
    """
    Homepage. It redirects to login if not authenticated, otherwise shows classes, calendar and weather 
    """
    if current_user.is_authenticated:
        user = current_user
        user_data = app.config['USERS_COLLECTION'].find_one({"_id": user._id})
        classes = []
        id_list = user_data.get('class_id_list')
        for class_id in id_list:
            classes.append(app.config['CLASS_COLLECTION'].find_one({"_id": class_id}))
        classes = list(reversed(classes))
        return render_template('home.html', user=user, classes=classes,
                               time=datetime.now().strftime('%b %d, %Y'))
    else:
        return redirect(url_for("login"))


@login_required
@app.route('/class/<class_id>')
def class_page(class_id):
    """
    Class page. It redirects to not enrolled if the user isn't in the class. 
    Lists assignments as well as links to grades, syllabus, etc. 
    """
    if current_user.is_authenticated:
        user = current_user
        user_data = app.config['USERS_COLLECTION'].find_one({"_id": user._id})
        id_list = user_data.get('class_id_list')
        if class_id not in id_list:
            flash("You are not enrolled in this class!", category='error')
            return redirect(url_for("home"))
        class_data = app.config['CLASS_COLLECTION'].find_one({"_id": class_id})
        prof = class_data.get('professor_id')
        assignments = []
        id_list = class_data.get('assignment_id_list')
        for assign_id in id_list:
            assignments.append(app.config['ASSIGNMENT_COLLECTION'].find_one({"_id": assign_id}))
        assignments = list(reversed(assignments))
        return render_template('class_page.html', assignments=assignments, class_name=class_id, professor=prof,
                               time=datetime.now().strftime('%b %d, %Y'))
    else:
        return redirect(url_for("login"))


@login_required
@app.route('/grades/<class_id>')
def grades_page(class_id):
    """
    Lists the users grades for their assignments in a class
    """
    if current_user.is_authenticated:
        user = current_user
        user_data = app.config['USERS_COLLECTION'].find_one({"_id": user._id})
        id_list = user_data.get('class_id_list')
        if class_id not in id_list:
            flash("You are not enrolled in this class!", category='error')
            return redirect(url_for("home"))
        class_data = app.config['CLASS_COLLECTION'].find_one({"_id": class_id})
        prof = class_data.get('professor_id')
        assignments = []
        id_list = class_data.get('assignment_id_list')
        for assign_id in id_list:
            assignments.append(app.config['ASSIGNMENT_COLLECTION'].find_one({"_id": assign_id}))
        assignments = list(reversed(assignments))

        assignment_grades = []
        for assignment in assignments:
            id_list = assignment.get('grade_id_list')
            for id in id_list:
                grade = app.config['GRADE_COLLECTION'].find_one({"_id": id})
                if grade.get('parent_user_id') == user._id:
                    assignment_grades.append([assignment.get('_id'), grade.get('grade')])

        return render_template('grades_page.html', assignment_grades=assignment_grades, class_name=class_id,
                               time=datetime.now().strftime('%b %d, %Y'))
    else:
        return redirect(url_for("login"))


@login_required
@app.route('/assignment/<class_id>?assignment_id=<assignment_id>', methods=['GET', 'POST'])
def assignment_page(class_id, assignment_id):
    """
    Submission page for the assignment. Shows previous submission and current grade if they exist. 
    """
    if current_user.is_authenticated:
        user = current_user
        form = AssignmentForm()
        if request.method == 'POST':
            if form.validate_on_submit():
                text = form.submission.data
                grade = app.config['GRADE_COLLECTION'].find_one({"parent_user_id": user._id,
                                                                 "parent_assignment_id": assignment_id})
                if grade is None:
                    app.config['GRADE_COLLECTION'].insert({"parent_user_id": user._id,
                                                           "parent_assignment_id": assignment_id, "submission": ""})

                app.config['GRADE_COLLECTION'].find_one_and_update({"parent_user_id": user._id,
                                                                    "parent_assignment_id": assignment_id},
                                                                   {'$set': {'submission': text}})

                flash("Submitted successfully!", category='success')
                return redirect(url_for("assignment_page", class_id=class_id, assignment_id=assignment_id))
            else:
                flash("Error!", category='error')
                return redirect(url_for("assignment_page"))

        user_data = app.config['USERS_COLLECTION'].find_one({"_id": user._id})
        assignment = app.config['ASSIGNMENT_COLLECTION'].find_one({"_id": assignment_id})
        if assignment is None:
            flash('Assignment not found', category='error')
            redirect(url_for("class_page", class_id=class_id))
        id_list = assignment.get('grade_id_list')
        grade = None
        if id_list is not None:
            for grade_id in id_list:
                temp_grade = app.config['GRADE_COLLECTION'].find_one({"_id": grade_id})
                if temp_grade is not None:
                    if user_data.get('_id') == temp_grade.get('parent_user_id'):
                        grade = temp_grade

        submission = None
        if grade is not None:
            if grade.get('submission') is not None:
                submission = grade.get('submission')

        return render_template('assignment_page.html', assignment_name=assignment_id, grade=grade.get('grade'),
                               submission=submission, time=datetime.now().strftime('%b %d, %Y'), form=form)
    else:
        return redirect(url_for("login"))


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Login page. Validates login and contains form. 
    """
    if current_user is not None and current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = app.config['USERS_COLLECTION'].find_one({"_id": form.username.data})
        if user and User.validate_login(user['password'], form.password.data):
            user_obj = User(user['_id'])
            login_user(user_obj)
            flash("Logged in successfully!", category='success')
            return redirect(url_for("home"))
        flash("Wrong username or password!", category='error')
    return render_template('login.html', title='login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/authorize/<provider>')
def oauth_authorize(provider):
    """
    Check if user is authorized from google sign-in 
    """
    if not current_user.is_anonymous:
        return redirect(url_for('home'))
    oauth = OAuthSignIn.get_provider(provider)
    return oauth.authorize()


@app.route('/callback/<provider>')
def oauth_callback(provider):
    """
    Redirects to google and returns the username and email of the user.
    """
    if not current_user.is_anonymous:
        return redirect(url_for('home'))
    oauth = OAuthSignIn.get_provider(provider)
    username, email = oauth.callback()
    if email is None:
        flash("Wrong username or password!", category='error')
        return redirect(url_for('login'))
    user = app.config['USERS_COLLECTION'].find_one({"_id": email})
    if not user:
        flash("Not a valid user", category='error')
        return redirect(url_for('login'))

    user_obj = User(user['_id'])
    login_user(user_obj)
    flash("Logged in successfully!", category='success')
    return redirect(url_for('home'))


@lm.user_loader
def load_user(username):
    u = app.config['USERS_COLLECTION'].find_one({"_id": username})
    if not u:
        return None
    return User(u['_id'])
