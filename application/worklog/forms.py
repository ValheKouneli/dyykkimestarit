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
    #Ei muokattavissa - readonly
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
    #Ei muokattavissa - readonly
    account_id = IntegerField("Kirjaajan henkilönumero: ")
    id = IntegerField("Työtehtävän kirjausnumero: ")
    task = StringField("Työtehtävän kuvaus: ")
    task_id = StringField("Työtehtävän tunnistenumero: ")
    worked_hours = IntegerField("Tehtävälle kirjatut työtunnit: ")

    class Meta:
        csrf = False

#Tulevat työtehtävät
class UpcomingForm(FlaskForm):
    name = StringField("Anna työtehtävälle nimi: ", [validators.Length(min=5)])
    date = DateField("Anna työtehtävän päivämäärä muodossa päivä.kuukausi.vuosi: ", format='%d.%m.%Y', render_kw={"placeholder": "01.01.1970"})
    hours = IntegerField("Arvioi työtehtävän kesto tunneissa: ", [validators.Required(message="Syötä työtunnit!")])
    account_id = SelectField(u'Työlle suunniteltu työntekijä: ', coerce=int)

    class Meta:
        csrf = False