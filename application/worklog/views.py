from application import app
from flask import render_template, request

@app.route("/worklog/new")
def worklog_form():
    return render_template("worklog/new.html")

@app.route("/worklog/", methods=["POST"])
def worklog_create():
    print(request.form.get("id"))

    return "PLACEHOLDER"