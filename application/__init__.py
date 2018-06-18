from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import current_user

app = Flask(__name__)
bcrypt = Bcrypt(app)

#Herokun ja lokaalin tietokannan määrittelyt
if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dyykki.db"
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app) 

#Kirjautuminen
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Kirjaudu sisään nähdäksesi tämän sivun"

# roles in login_required
from functools import wraps

def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user.is_authenticated:
                return login_manager.unauthorized()
            
            unauthorized = False

            if role != "ANY":
                unauthorized = True
                
                for user_role in current_user.roles():
                    if user_role == role:
                        unauthorized = False
                        break

            if unauthorized:
                return login_manager.unauthorized()
            
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper


from application import views

#Listauksen/sovelluksen importit
from application.worklog import models
from application.worklog import views

#Autentikaation importit
from application.auth import models
from application.auth import views

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

#Tietokannan luonti
db.create_all()