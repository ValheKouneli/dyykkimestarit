from application import db

class WorkDone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    worker_id = db.Column(db.Integer, nullable=False)
    task = db.Column(db.String(144), nullable=False)
    task_id = db.Column(db.Integer, nullable=True)
    worked_hours = db.Column(db.Integer, nullable=False)

    def __init__(self, worker_id, task, task_id, worked_hours):
        self.worker_id = worker_id
        self.task = task
        self.task_id = task_id
        self.worked_hours = worked_hours

class PlannedWork(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(144), nullable=False)
    date = db.Column(db.String(144), nullable=False)
    worker_one = db.Column(db.Integer, nullable=False)
    worker_two = db.Column(db.Integer, nullable=True)

    def __init__(self, name, date, worker_one, worker_two):
        self.name = name
        self.date = date
        self.worker_one = worker_one
        self.worker_two = worker_two

class Employees(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(144), nullable=False)
    courses = db.Column(db.String(144), nullable=False)

    def __init__(self, name):
        self.name = name
        self.courses = DM

