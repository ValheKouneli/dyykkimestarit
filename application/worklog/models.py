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
    task_id = db.Column(db.Integer, nullable=True)
    worked_hours = db.Column(db.Integer, nullable=False)

    def __init__(self, account_id, task, task_id, worked_hours):
        self.account_id = account_id
        self.task = task
        self.task_id = task_id
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

    def __init__(self, account_id, name, date, hours):
        self.account_id = account_id
        self.name = name
        self.date = date
        self.hours = hours

#Suunnitellut työtehtävät liitostaulu - HAHMOTELMA
class PlannedWork(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey("account.id"), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey("upcoming_work.id"), nullable=False)
