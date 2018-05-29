from flask import render_template, request, redirect, url_for

from application import app, db
from application.worklog.models import WorkDone
from application.worklog.forms import WorkForm, EditForm

#Listaus
@app.route("/worklog", methods=["GET"])
def worklog_index():
    return render_template("worklog/list.html", worklog = WorkDone.query.all())

#Uuden työtehtävän kirjaussivu
@app.route("/worklog/new")
def worklog_form():
    return render_template("worklog/new.html", form=WorkForm())

#Uuden työtehtävän POST
@app.route("/worklog/", methods=["POST"])
def worklog_create():
    form = WorkForm(request.form)

    new = WorkDone(form.id.data, form.task.data, form.task_id.data, form.hours.data)

    db.session().add(new)
    db.session().commit()

    return redirect(url_for("worklog_index"))

#Työtehtävän muokkaaminen
@app.route("/worklog/<work_id>/", methods=["GET", "POST"])
def worklog_edit(work_id):
    work = WorkDone.query.get(work_id)
    form = EditForm(obj=work)

    if  request.method == 'POST':
        editform = EditForm(request.form)

        work.task = editform.task.data
        work.task_id = editform.task_id.data
        work.worked_hours = editform.worked_hours.data

        db.session().commit()

        return redirect(url_for("worklog_index"))
    else:
        
        return render_template("worklog/edit.html", w = WorkDone.query.get(work_id), form=form)


