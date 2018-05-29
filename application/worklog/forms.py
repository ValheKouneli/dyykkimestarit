from flask_wtf import FlaskForm
from wtforms import StringField

class WorkForm(FlaskForm):
    id = StringField("Anna henkilönumerosi: ")
    task = StringField("Kuvaile työtehtävän sisältöä: ")
    task_id = StringField("Anna työtehtävän mahdollinen tunnistenumero: ")
    hours = StringField("Kuinka monta tuntia työskentelit? ")

    class Meta:
        csrf = False

class EditForm(FlaskForm):
    #Ei muokattavissa
    worker_id = StringField("Henkilönumerosi: ")
    id = StringField("Työtehtävän kirjausnumero: ")

    #Muokattavissa
    task = StringField("Muokkaa työtehtävän kuvausta: ")
    task_id = StringField("Muokkaa työtehtävän tunnistenumeroa: ")
    worked_hours = StringField("Muokkaa tehtyjä työtunteja: ")

    class Meta:
        csrf = False


