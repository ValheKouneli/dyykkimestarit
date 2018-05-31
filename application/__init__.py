from flask import Flask
app = Flask(__name__)

import os
from flask_sqlalchemy import SQLAlchemy

#Herokun ja lokaalin tietokannan määrittelyt
if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dyykki.db"
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app) 

from application import views

#Listauksen/sovelluksen importit
from application.worklog import models
from application.worklog import views

#Autentikaation importit
from application.auth import models
from application.auth import views

#Kirjautuminen
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Kirjaudu sisään nähdäksesi tämän sivun"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

#Tietokannan luonti
try:
    db.create_all()
except:
    pass