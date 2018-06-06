from application import db

from sqlalchemy.sql import text

class User(db.Model):

    __tablename__ = "account"

    id = db.Column(db.Integer, primary_key=True)

    #Kirjautumistiedot
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    #Muut tiedot
    name = db.Column(db.String(144), nullable=False)
    certificates = db.Column(db.String(144), nullable=False)

    #Tehtävät
    work = db.relationship("WorkDone", backref='account', lazy=True)

    def __init__(self, username, password, name, certificates):
        self.username = username
        self.password = password

        self.name = name
        self.certificates = certificates

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

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