from application import db

from sqlalchemy.sql import text

#Tehdyt työtehtävät tietokantataulu
class WorkDone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.Date, default=db.func.current_date())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    #Kirjauksen tehneen käyttäjän id
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    task = db.Column(db.String(144), nullable=False)
    task_type = db.Column(db.String(144), nullable=True)
    worked_hours = db.Column(db.Integer, nullable=False)

    def __init__(self, account_id, task, task_type, worked_hours):
        self.account_id = account_id
        self.task = task
        self.task_type = task_type
        self.worked_hours = worked_hours

    #Kaikki tunnit, olisi varmaan generoitavissa alchemylla mutta SQL harjoittelua
    @staticmethod
    def total_hours():
        stmt = text("SELECT SUM(worked_hours) FROM work_done")

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"total_hours":row[0]})

        return response

    #Kirjautuneen käyttäjän tunnit
    @staticmethod
    def user_hours(user):
        stmt = text("SELECT SUM(worked_hours) FROM work_done"
                    " LEFT JOIN account ON account.id = work_done.account_id"
                    " WHERE (account.id = :id)").params(id=user.id)

        print(stmt)

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"user_hours":row[0]})

        return response

#Tulevat kurssit
class UpcomingWork(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, nullable=False)

    name = db.Column(db.String(144), nullable=False)
    date = db.Column(db.Date, nullable=False)
    hours = db.Column(db.Integer, nullable=False)

    users = db.relationship("User", secondary="planned_work", backref="work")

    def __init__(self, account_id, name, date, hours):
        self.account_id = account_id
        self.name = name
        self.date = date
        self.hours = hours

    #Olisi ehkä toteutettavissa ormin kautta kuten toinenkin, mutta halusin verrata filter_by ja WHERE tuloksia
    @staticmethod
    def select_filtered(user):
        stmt = text("SELECT * FROM upcoming_work"
                    " WHERE (account_id = :id)").params(id=user.id)
        
        res = db.engine.execute(stmt)

        response = []

        for row in res:
            response.append({ "id":row[0], "account_id":row[1], "name":row[2], "date":row[3], "hours":row[4] })

        return response

#Suunnitellut työtehtävät liitostaulu
class PlannedWork(db.Model):
    account_id = db.Column(db.Integer, db.ForeignKey("account.id"), nullable=False, primary_key = True)
    course_id = db.Column(db.Integer, db.ForeignKey("upcoming_work.id"), nullable=False, primary_key = True)

