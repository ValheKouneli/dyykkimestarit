from application import app, db
from flask import render_template, request, redirect, url_for
from application.worklog.models import WorkDone

#Listaus
@app.route("/worklog", methods=["GET"])
def worklog_index():
    return render_template("worklog/list.html", worklog = WorkDone.query.all())

#Uuden työtehtävän kirjaussivu
@app.route("/worklog/new")
def worklog_form():
    return render_template("worklog/new.html")

#Uuden työtehtävän POST
@app.route("/worklog/", methods=["POST"])
def worklog_create():
    id = request.form.get("id")
    task = request.form.get("task")
    task_id = request.form.get("task_id")
    hours = request.form.get("worked_hours")

    new = WorkDone(id, task, task_id, hours)

    db.session().add(new)
    db.session().commit()

    return redirect(url_for("worklog_index"))