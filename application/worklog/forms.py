from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class WorkForm(FlaskForm):
    #IntegerField hoitaa validoinnin kokonaisluvuksi
    worker_id = IntegerField("Anna henkilönumerosi: ")
    task = StringField("Kuvaile työtehtävän sisältöä: ", [validators.Length(min=5)])
    task_id = IntegerField("Anna työtehtävän mahdollinen tunnistenumero: ", [validators.Optional()])
    worked_hours = IntegerField("Kuinka monta tuntia työskentelit? ")

    class Meta:
        csrf = False

class EditForm(FlaskForm):
    #Ei muokattavissa
    worker_id = IntegerField("Henkilönumerosi: ")
    id = IntegerField("Työtehtävän kirjausnumero: ")

    #Muokattavissa
    task = StringField("Muokkaa työtehtävän kuvausta: ", [validators.Length(min=5)])
    task_id = IntegerField("Muokkaa työtehtävän tunnistenumeroa: ", [validators.Optional()])
    worked_hours = IntegerField("Muokkaa tehtyjä työtunteja: ")

    class Meta:
        csrf = False


