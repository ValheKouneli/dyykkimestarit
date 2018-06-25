from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user

from application import app, db, bcrypt, login_required
from application.auth.models import User
from application.auth.forms import LoginForm, RegisterForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm() )
    
    else:
        form = LoginForm(request.form)
        if not form.validate():
            return render_template("auth/loginform.html", form = form )
        
        user = User.query.filter_by(username=form.username.data).first()

        if user is None:
            return render_template("auth/loginform.html", form = LoginForm())

        if user.is_correct_password(form.password.data):
            login_user(user)

            return redirect(url_for("worklog_stats"))
        else:
            return render_template("auth/loginform.html", form = form, error = "Käyttäjänimi tai salasana väärin")
        

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/auth/register", methods = ["GET", "POST"])
@login_required(role="ADMIN")
def auth_register():

    if request.method == "GET":
        return render_template("auth/register.html", form = RegisterForm())
    
    else:
        form = RegisterForm(request.form)

        if not form.validate():
            return render_template("auth/register.html", form = form)

        new = User(form.username.data, bcrypt.generate_password_hash(form.plaintext_password.data).decode('utf-8'), form.name.data, form.certificates.data, form.roles.data)

        db.session().add(new)
        db.session().commit()

        return redirect(url_for("worklog_stats"))