from flask import Flask
from flask_login import LoginManager
from pymongo import MongoClient
"""
Setup for the app, loginmanager and database
"""


app = Flask(__name__)
app.config.from_object('config')

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

client = MongoClient()
db = client['final0db']

from app import views
