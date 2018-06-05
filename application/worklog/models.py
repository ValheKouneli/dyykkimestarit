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

    def __init__(self, worker_id, task, task_id, worked_hours):
        self.worker_id = worker_id
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



#Tulevat kurssit - Hahmotelma
class UpcomingWork(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(144), nullable=False)
    date = db.Column(db.Date, nullable=False)
    first_worker = db.Column(db.Integer, nullable=False)
    second_worker = db.Column(db.Integer, nullable=True)
    hours = db.Column(db.Integer, nullable=False)
    def __init__(self, name, date, second_worker, hours):
        self.name = name
        self.date = date
        self.second_worker = second_worker
        self.hours = hours

#Suunnitellut työtehtävät liitostaulu - HAHMOTELMA
class PlannedWork(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey("account.id"), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey("upcoming_work.id"), nullable=False)
