from flask_wtf import FlaskForm
from wtforms import StringField

class WorkForm(FlaskForm):
    id = StringField("Anna henkilönumerosi: ")
    task = StringField("Kuvaile työtehtävän sisältöä: ")
    task_id = StringField("Anna työtehtävän mahdollinen tunnistenumero: ")
    hours = StringField("Kuinka monta tuntia työskentelit? ")

    class Meta:
        csrf = False

