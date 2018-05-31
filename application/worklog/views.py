from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.worklog.models import WorkDone
from application.worklog.forms import WorkForm, EditForm

#Listaus
@app.route("/worklog", methods=["GET"])
@login_required
def worklog_index():
    return render_template("worklog/list.html", worklog = WorkDone.query.all())

#Uuden työtehtävän kirjaussivu
@app.route("/worklog/new")
@login_required
def worklog_form():
    return render_template("worklog/new.html", form=WorkForm())

#Uuden työtehtävän POST
@app.route("/worklog/", methods=["POST"])
@login_required
def worklog_create():
    form = WorkForm(request.form)

    #Validoinnin tarkastus
    if not form.validate():
        return render_template("/worklog/new.html", form=form)

    new = WorkDone(1, form.task.data, form.task_id.data, form.worked_hours.data)
    new.account_id = current_user.id    

    db.session().add(new)
    db.session().commit()

    return redirect(url_for("worklog_index"))

#Työtehtävän muokkaaminen
@app.route("/worklog/<work_id>/", methods=["GET", "POST"])
@login_required
def worklog_edit(work_id):
    work = WorkDone.query.get(work_id)
    form = EditForm(obj=work)

    if  request.method == 'POST':
        editform = EditForm(request.form)

        #Validoinnin tarkastus
        if not editform.validate():
            return render_template("worklog/edit.html", w = WorkDone.query.get(work_id), form=editform)

        work.task = editform.task.data
        work.task_id = editform.task_id.data
        work.worked_hours = editform.worked_hours.data

        db.session().commit()

        return redirect(url_for("worklog_index"))
    else:
        return render_template("worklog/edit.html", w = WorkDone.query.get(work_id), form=form)


