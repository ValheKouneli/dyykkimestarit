from application import db

class User(db.Model):

    __tablename__ = "account"

    id = db.Column(db.Integer, primary_key=True)

    #Kirjautumistiedot
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    #Muut tiedot
    name = db.Column(db.String(144), nullable=False)
    certificates = db.Column(db.String(144), nullable=False)

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

