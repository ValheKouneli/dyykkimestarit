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
        edit = WorkDone.query.get(work_id)
        edit.worker_id = request.form.get("worker_id")
        edit.task = request.form.get("task")
        edit.task_id = request.form.get("task_id")
        edit.worked_hours = request.form.get("worked_hours")

        db.session().commit()

        return redirect(url_for("worklog_index"))
    else:
        
        return render_template("worklog/edit.html", w = WorkDone.query.get(work_id), form=form)


