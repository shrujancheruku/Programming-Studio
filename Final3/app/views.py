from app import app, lm, fs
from flask import request, redirect, render_template, url_for, flash, make_response
from flask_login import login_user, logout_user, current_user, login_required
from .forms import LoginForm, AssignmentForm, CreateAssignmentForm, AddTAForm, JSONForm, SyllabusForm, AnnouncementForm
from .models import User
from .auth import OAuthSignIn
from datetime import datetime
from bson import ObjectId
from app import parseJSON
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
        if id_list is not None:
            for assign_id in id_list:
                assignments.append(app.config['ASSIGNMENT_COLLECTION'].find_one({"_id": assign_id}))
        assignments = list(reversed(assignments))
        ta_list = class_data.get('ta_list')
        return render_template('class_page.html', assignments=assignments, class_name=class_id, professor=prof,
                               time=datetime.now().strftime('%b %d, %Y'), user=user, ta_list=ta_list)
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
                    assignment_grades.append([assignment.get('name'), grade.get('grade')])

        return render_template('grades_page.html', assignment_grades=assignment_grades, class_name=class_id,
                               time=datetime.now().strftime('%b %d, %Y'))
    else:
        return redirect(url_for("login"))


@login_required
@app.route('/assignment/<class_id>?<assignment_id>', methods=['GET', 'POST'])
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
                                                                 "parent_assignment_id": ObjectId(assignment_id)})
                if grade is None:
                    app.config['GRADE_COLLECTION'].insert({"parent_user_id": user._id,
                                                           "parent_assignment_id": ObjectId(assignment_id), "submission": ""})

                    grade = app.config['GRADE_COLLECTION'].find_one({"parent_user_id": user._id,
                                                                     "parent_assignment_id": ObjectId(assignment_id)})

                    app.config['ASSIGNMENT_COLLECTION'].find_one_and_update({'_id': ObjectId(assignment_id)},
                                                                            {'$push': {'grade_id_list': grade.get('_id')}})
                file_id = None
                if form.file.data:
                        submission_file = request.files[form.file.name]
                        file_id = fs.put(submission_file)

                app.config['GRADE_COLLECTION'].find_one_and_update({"parent_user_id": user._id,
                                                                    "parent_assignment_id": ObjectId(assignment_id)},
                                                                   {'$set': {'submission': text,
                                                                             'submission_file': file_id}})

                flash("Submitted successfully!", category='success')
                return redirect(url_for("assignment_page", class_id=class_id, assignment_id=assignment_id))
            else:
                flash("Error!", category='error')
                return redirect(url_for("assignment_page", class_id=class_id, assignment_id=assignment_id))

        user_data = app.config['USERS_COLLECTION'].find_one({"_id": user._id})
        assignment = app.config['ASSIGNMENT_COLLECTION'].find_one({"_id": ObjectId(assignment_id)})

        if assignment is None:
            flash('Assignment not found', category='error')
            return redirect(url_for("class_page", class_id=class_id))

        id_list = assignment.get('grade_id_list')
        grade = None
        if id_list is not None:
            for grade_id in id_list:
                temp_grade = app.config['GRADE_COLLECTION'].find_one({"_id": grade_id})
                if temp_grade is not None:
                    if user_data.get('_id') == temp_grade.get('parent_user_id'):
                        grade = temp_grade

        submission = None
        grade_val = None
        file_sub = None
        if grade is not None:
            grade_val = grade.get('grade')
            if grade.get('submission') is not None:
                submission = grade.get('submission')
            if grade.get('submission_file') is not None:
                file_sub = grade.get('submission_file')
        return render_template('assignment_page.html', assignment_name=assignment.get('name'), grade=grade_val,
                               submission=submission, file=file_sub, time=datetime.now().strftime('%b %d, %Y'),
                               form=form, info=assignment.get('info'), class_id=class_id)
    else:
        return redirect(url_for("login"))


@login_required
@app.route('/syllabus_view/<class_id>', methods=['GET'])
def syllabus(class_id):
    class_data = app.config['CLASS_COLLECTION'].find_one({"_id": class_id})
    if class_data.get('syllabus') is not None:
        syllabus_id = class_data.get('syllabus')
        return redirect(url_for("show_index", oid=syllabus_id))

    return redirect(url_for('class_page', class_id=class_id))

@login_required
@app.route('/admin/<class_id>', methods=['GET', 'POST'])
def admin_page(class_id):

    assignment_form = CreateAssignmentForm()
    ta_form = AddTAForm()
    json_form = JSONForm()
    syllabus_form = SyllabusForm()
    announcement_form = AnnouncementForm()
    if request.method == 'POST':
        if assignment_form.submit1.data:
            if assignment_form.validate_on_submit():
                app.config['ASSIGNMENT_COLLECTION'].insert({"name": assignment_form.name.data, 'parent_class_id': class_id,
                                                            'grade_id_list': [], "info": assignment_form.info.data})

                assign = app.config['ASSIGNMENT_COLLECTION'].find_one({"name": assignment_form.name.data})

                app.config['CLASS_COLLECTION'].find_one_and_update({'_id': class_id},
                                                                   {'$push': {'assignment_id_list': assign.get('_id')}})
                flash("Assignment Created!", category='success')
                return redirect(url_for("admin_page", class_id=class_id))
            else:
                flash("Error Creating Assignment", category='error')
                return redirect(url_for("admin_page", class_id=class_id))

        elif ta_form.submit2.data:
            if ta_form.validate_on_submit():
                app.config['CLASS_COLLECTION'].find_one_and_update({'_id': class_id},
                                                                   {'$push': {'ta_list': ta_form.username.data}})
                flash("TA Added!", category='success')
                return redirect(url_for("admin_page", class_id=class_id))
            else:
                flash("Error Adding TA", category='error')
                return redirect(url_for("admin_page", class_id=class_id))
        elif json_form.submit3.data:
            if json_form.validate_on_submit():
                submission_file = request.files[json_form.file.name]
                student_data = parseJSON.get_students(submission_file)
                for student in student_data:
                    app.config['USERS_COLLECTION'].find_one_and_update({'_id': student},
                                                                       {'$push': {'class_id_list': class_id}},
                                                                       upsert=True)

                    app.config['CLASS_COLLECTION'].find_one_and_update({'_id': class_id},
                                                                       {'$push': {'student_id_list': student}})

                flash("Roster Added!", category='success')
                return redirect(url_for("admin_page", class_id=class_id))
            else:
                flash("Error Adding Roster", category='error')
                return redirect(url_for("admin_page", class_id=class_id))

        elif syllabus_form.submit4.data:
            if syllabus_form.validate_on_submit():
                file_id = None
                if syllabus_form.file.data:
                    submission_file = request.files[syllabus_form.file.name]
                    file_id = fs.put(submission_file)
                app.config['CLASS_COLLECTION'].find_one_and_update({'_id': class_id}, {'$set': {'syllabus': file_id}},
                                                                   upsert=True)

                flash("Syllabus Added!", category='success')
                return redirect(url_for("admin_page", class_id=class_id))
            else:
                flash("Error Adding Syllabus", category='error')
                return redirect(url_for("admin_page", class_id=class_id))

        elif announcement_form.submit5.data:
            if announcement_form.validate_on_submit():
                announcement = announcement_form.text.data
                app.config['CLASS_COLLECTION'].find_one_and_update({'_id': class_id},
                                                                   {'$push': {'announcements': announcement}},
                                                                   upsert=True)

                flash("Announcement Added!", category='success')
                return redirect(url_for("admin_page", class_id=class_id))
            else:
                flash("Error Adding Announcement", category='error')
                return redirect(url_for("admin_page", class_id=class_id))

        else:
            flash("Error", category='error')
            return redirect(url_for("admin_page", class_id=class_id))

    class_data = app.config['CLASS_COLLECTION'].find_one({"_id": class_id})
    prof = class_data.get('professor_id')
    user = current_user._id
    id_list = class_data.get('assignment_id_list')
    if user == prof:
        return render_template('admin_page.html', class_id=class_id, professor=prof, user=user,
                               assignment_form=assignment_form, ta_form=ta_form, json_form=json_form,
                               syllabus_form=syllabus_form, announcement_form=announcement_form, list=id_list,
                               time=datetime.now().strftime('%b %d, %Y'))
    else:
        flash("Not Authorized", category='error')
        return redirect(url_for("home"))


@login_required
@app.route('/syllabus/<class_id>', methods=['GET', 'POST'])
def syllabus_page(class_id):

    assignment_form = CreateAssignmentForm()
    if request.method == 'POST':
        if assignment_form.validate_on_submit():
            app.config['ASSIGNMENT_COLLECTION'].insert({"name": assignment_form.name.data, 'parent_class_id': class_id,
                                                            'grade_id_list': [], "info": assignment_form.info.data})
            assign = app.config['ASSIGNMENT_COLLECTION'].find_one({"name": assignment_form.name.data})

            app.config['CLASS_COLLECTION'].find_one_and_update({'_id': class_id},
                                                                   {'$push': {'assignment_id_list': assign.get('_id')}})
            flash("Assignment Created!", category='success')
            return render_template("syllabus_page.html", class_id=class_id, assignment_form=assignment_form,
                                   time=datetime.now().strftime('%b %d, %Y'))
        else:
            flash("Error Creating Assignment", category='error')
            return render_template("syllabus_page.html", class_id=class_id, assignment_form=assignment_form,
                                   time=datetime.now().strftime('%b %d, %Y'))

    class_data = app.config['CLASS_COLLECTION'].find_one({"_id": class_id})
    prof = class_data.get('professor_id')
    user = current_user._id
    if user == prof:
        return render_template("syllabus_page.html", class_id=class_id, assignment_form=assignment_form,
                               time=datetime.now().strftime('%b %d, %Y'))
    else:
        flash("Not Authorized", category='error')
        return redirect(url_for("home"))


@login_required
@app.route('/announcements/<class_id>', methods=['GET'])
def announcements_page(class_id):
    class_data = app.config['CLASS_COLLECTION'].find_one({"_id": class_id})
    announcements = class_data.get('announcements')
    announcements = list(reversed(announcements))
    return render_template("announcement_page.html", class_name=class_id, announcements=announcements,
                           time=datetime.now().strftime('%b %d, %Y'))


@login_required
@app.route('/grade/<class_id>', methods=['GET', 'POST'])
def grading_list_page(class_id):
    return ""


@login_required
@app.route('/grade/<class_id>/<assignment_id>', methods=['GET', 'POST'])
def grading_page(class_id, assignment_id):
    return ""


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
    return render_template('login.html', title='login', form=form, time=datetime.now().strftime('%b %d, %Y'))


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


@app.route('/showFile/<oid>')
def show_index(oid):
    grid_fs_file = fs.get(ObjectId(oid))
    response = make_response(grid_fs_file.read())
    response.headers['Content-Type'] = 'application/pdf'
    response.headers["Content-Disposition"] = "attachment; filename={}".format("Submission.pdf")
    return response


@lm.user_loader
def load_user(username):
    u = app.config['USERS_COLLECTION'].find_one({"_id": username})
    if not u:
        return None
    return User(u['_id'])
