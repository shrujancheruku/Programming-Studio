from app import app, lm, db
from flask import request, redirect, render_template, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from .forms import LoginForm
from .models import User
from .auth import OAuthSignIn
"""
Views for the Flask app. Contains the routes for the page routing
"""


@login_required
@app.route('/')
def home():
    if current_user.is_authenticated:
        return render_template('home.html')
    else:
        return redirect(url_for("login"))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user is not None and current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = app.config['USERS_COLLECTION'].find_one({"username": form.username.data})
        if user and User.validate_login(user['password'], form.password.data):
            user_obj = User(user['username'])
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
    if not current_user.is_anonymous:
        return redirect(url_for('home'))
    oauth = OAuthSignIn.get_provider(provider)
    return oauth.authorize()


@app.route('/callback/<provider>')
def oauth_callback(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('index'))
    oauth = OAuthSignIn.get_provider(provider)
    username, email = oauth.callback()
    if email is None:
        flash("Wrong username or password!", category='error')
        return redirect(url_for('login'))
    user = app.config['USERS_COLLECTION'].find_one({"username": email})
    if not user:
        user = User(username=email)
        db.users.insert({"username": email})

    user_obj = User(user['username'])
    login_user(user_obj)
    flash("Logged in successfully!", category='success')
    return redirect(url_for('home'))


@lm.user_loader
def load_user(username):
    u = app.config['USERS_COLLECTION'].find_one({"username": username})
    if not u:
        return None
    return User(u['username'])
