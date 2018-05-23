from flask import Flask
app = Flask(__name__)

#SQLAlchemy määrittelyt ja SQLite tietokanta
from flask_sqlalchemy import SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dyykki.db"
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app) 

from application import views

from application.worklog import models
from application.worklog import views

db.create_all()