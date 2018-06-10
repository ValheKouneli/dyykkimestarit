from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators, DateField, SelectField

class WorkForm(FlaskForm):
    #IntegerField hoitaa validoinnin kokonaisluvuksi
    task = StringField("Kuvaile työtehtävän sisältöä: ", [validators.Length(min=5)])
    task_id = IntegerField("Anna työtehtävän mahdollinen tunnistenumero: ", [validators.Optional()])
    worked_hours = IntegerField("Kuinka monta tuntia työskentelit? ")

    class Meta:
        csrf = False

class EditForm(FlaskForm):
    #Ei muokattavissa
    account_id = IntegerField("Henkilönumerosi: ")
    id = IntegerField("Työtehtävän kirjausnumero: ")

    #Muokattavissa
    task = StringField("Muokkaa työtehtävän kuvausta: ", [validators.Length(min=5)])
    task_id = IntegerField("Muokkaa työtehtävän tunnistenumeroa: ", [validators.Optional()])
    worked_hours = IntegerField("Muokkaa tehtyjä työtunteja: ")

    class Meta:
        csrf = False

#Toteutettu readonly formina yksinkertaisuuden ja yhtenevien näkymien vuosi
class SingleForm(FlaskForm):
    #readonly
    account_id = IntegerField("Kirjaajan henkilönumero: ")
    id = IntegerField("Työtehtävän kirjausnumero: ")
    task = StringField("Työtehtävän kuvaus: ")
    task_id = StringField("Työtehtävän tunnistenumero: ")
    worked_hours = IntegerField("Tehtävälle kirjatut työtunnit: ")

    class Meta:
        csrf = False

class UpcomingForm(FlaskForm):
    name = StringField("Anna työtehtävälle nimi: ", [validators.Length(min=5)])
    date = DateField("Anna työtehtävän päivämäärä muodossa vuosi-kuukausi-päivä: ")
    hours = IntegerField("Arvioi työtehtävän kesto tunneissa: ")
    account_id = SelectField(u'Työlle suunniteltu työntekijä: ', coerce=int)

    class Meta:
        csrf = False