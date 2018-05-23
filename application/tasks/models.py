from application import db

class WorkDone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    worker_id=db.Column(db.Integer, nullable=False)
    task=db.Column(db.String(144), nullable=False)
    task_id=db.Column(db.Integer, nullable=False)
    worked_hours=db.Column(db.Integer, nullable=False)

    def __init__(self, name):
        self.worker_id = 1
        self.task = task
        self.task_id = 1
        self.worked_hours = 0

