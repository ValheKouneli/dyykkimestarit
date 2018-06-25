from application import db, bcrypt

from sqlalchemy.sql import text
from sqlalchemy.ext.hybrid import hybrid_property
from flask_login import UserMixin, AnonymousUserMixin

class User(db.Model, UserMixin):

    __tablename__ = "account"

    id = db.Column(db.Integer, primary_key=True)

    #Kirjautumistiedot
    username = db.Column(db.String(144), unique=True, nullable=False)
    _password = db.Column(db.String(144), nullable=False)

    #roolit
    role = db.Column(db.String(60), nullable=False)

    #Muut tiedot
    name = db.Column(db.String(144), nullable=False)
    certificates = db.Column(db.String(144), nullable=False)

    def __init__(self, username, plaintext_password, name, certificates, roles):
        self.username = username
        self._password = plaintext_password

        self.name = name
        self.certificates = certificates

        self.role = roles

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        l = []
        l.append(self.role)
        return l

    #Salasanan kryptaus
    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def set_password(self, plaintext):
        self._password = bcrypt.generate_password_hash(plaintext, 15).decode('utf-8')


    def is_correct_password(self, plaintext):
        return bcrypt.check_password_hash(self._password, plaintext)

    @staticmethod
    def total_tasks():
        stmt = text("SELECT COUNT(work_done.id) FROM work_done"
                    " LEFT JOIN account ON account.id = work_done.account_id")
        
        res = db.engine.execute(stmt)
        
        response = []
        for row in res:
            response.append({"count":row[0] })

        return response

    @staticmethod
    def user_tasks(user):
        stmt = text("SELECT COUNT(work_done.id) FROM work_done"
                " LEFT JOIN account ON account.id = work_done.account_id"
                " WHERE (account.id = :id)").params(id=user.id)

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"tasks":row[0]})

        return response

class AnonymousUser(AnonymousUserMixin):

    def roles(self):
        return ["NONE"]