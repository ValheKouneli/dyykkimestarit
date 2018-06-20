from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SelectField, validators

class LoginForm(FlaskForm):
    username = StringField("Käyttäjätunnus", [validators.Required(message="Käyttäjänimi puuttuu")])
    password = PasswordField("Salasana", [validators.Required(message="Salasana puuttuu")])

    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    username = StringField("Käyttäjätunnus:", [validators.Length(min=5)])
    plaintext_password = PasswordField("Salasana:", [validators.Length(min=5)])
    name = StringField("Nimesi:", [validators.Length(min=5)])
    certificates = StringField("Käymäsi kurssit (erota pilkulla):", [validators.Required(message="Kenttä ei voi olla tyhjä")])
    roles = StringField("Rooli järjestelmässä, ADMIN antaa järjestelmänvalvojan oikeudet: ")

    class Meta:
        csrf = False
