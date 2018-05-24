from application import db

#Tehdyt työtehtävät tietokantataulu
class WorkDone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.Date, default=db.func.current_date())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    #worker_id myöhemmin foreign_keyksi kun employees tietokanta tulee käyttöön
    worker_id = db.Column(db.Integer, nullable=False)
    task = db.Column(db.String(144), nullable=False)
    task_id = db.Column(db.Integer, nullable=True)
    worked_hours = db.Column(db.Integer, nullable=False)

    def __init__(self, worker_id, task, task_id, worked_hours):
        self.worker_id = worker_id
        self.task = task
        self.task_id = task_id
        self.worked_hours = worked_hours

#Tulevat kurssit - Hahmotelma
class UpcomingWork(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(144), nullable=False)
    date = db.Column(db.Date, nullable=False)
    second_worker = db.Column(db.Integer, nullable=True)
    hours = db.Column(db.Integer, nullable=False)
    def __init__(self, name, date, second_worker, hours):
        self.name = name
        self.date = date
        self.second_worker = second_worker
        self.hours = hours

#Suunnitellut työtehtävät liitostaulu - HAHMOTELMA
class PlannedWork(db.Model):
    key_id = db.Column(db.Integer, primary_key=True)
    worker_id = db.Column(db.Integer, db.ForeignKey("employees.id"), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey("upcoming_work.id"), nullable=False)



#Työntekijät tietokantataulu, käyttöön myöhemmin kirjautumisen yhteydessä!
class Employees(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(144), nullable=False)
    certificates = db.Column(db.String(144), nullable=False)

    def __init__(self, name, certificates):
        self.name = name
        self.certificates = certificates

