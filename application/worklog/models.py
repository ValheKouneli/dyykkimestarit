from application import db

class WorkDone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    worker_id = db.Column(db.Integer, nullable=False)
    task = db.Column(db.String(144), nullable=False)
    task_id = db.Column(db.Integer, nullable=True)
    worked_hours = db.Column(db.Integer, nullable=False)

    def __init__(self, task):
        self.worker_id = 1
        self.task = task
        self.task_id = 1
        self.worked_hours = 0

class PlannedWork(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(144), nullable=False)
    date = db.Column(db.String(144), nullable=False)
    worker_one = db.Column(db.Integer, nullable=False)
    worker_two = db.Column(db.Integer, nullable=True)

    def __init__(self, name):
        self.name = name
        self.date = "1.1.1970"
        self.worker_one = 1

class Employees(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(144), nullable=False)
    courses = db.Column(db.String(144), nullable=False)

    def __init__(self, name):
        self.name = name
        self.courses = DM

