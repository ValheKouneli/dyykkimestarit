from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class LoginForm(FlaskForm):
    username = StringField("Username", [validators.Required(message="Käyttäjänimi puuttuu")])
    password = PasswordField("Password", [validators.Required(message="Salasana puuttuu")])

    class Meta:
        csrf = False
