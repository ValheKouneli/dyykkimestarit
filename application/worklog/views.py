from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.worklog.models import WorkDone
from application.worklog.models import UpcomingWork
from application.auth.models import User
from application.worklog.forms import WorkForm, EditForm, SingleForm, UpcomingForm

#Etusivu
@app.route("/worklog", methods=["GET"])
@login_required
def worklog_stats():
    #Kirjautunut käyttäjä
    u = User.query.get(current_user.id)

    return render_template("worklog/front.html", user=u, total_work=User.total_tasks(), 
                            total_hours=WorkDone.total_hours(), user_hours=WorkDone.user_hours(u),
                            user_work = User.user_tasks(u), upcoming_work = UpcomingWork.select_filtered(u) )

#Yksittäinen työtehtävä
@app.route("/worklog/<work_id>/", methods=["GET"])
@login_required
def worklog_single(work_id):
    work = WorkDone.query.get(work_id)
    form = SingleForm(obj=work)

    return render_template("worklog/single.html", w = WorkDone.query.get(work_id), form=form)

#Listaus
@app.route("/worklog/list", methods=["GET"])
@login_required
def worklog_list():
    return render_template("worklog/list.html", worklog = WorkDone.query.all() )

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

    return redirect(url_for("worklog_list"))

#Työtehtävän muokkaaminen
@app.route("/worklog/<work_id>/edit", methods=["GET", "POST"])
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

        return redirect(url_for("worklog_list"))
    else:
        return render_template("worklog/edit.html", w = WorkDone.query.get(work_id), form=form)

#Työtehtävän poistaminen
@app.route("/worklog/<work_id>/delete", methods=["GET", "POST"])
@login_required
def worklog_delete(work_id):
    work = WorkDone.query.get(work_id)

    db.session().delete(work)
    db.session().commit()

    return redirect(url_for("worklog_list"))

#Suunnitellun työtehtävän luominen
#Admin restricted - WIP
@app.route("/worklog/upcoming/", methods=["GET", "POST"])
@login_required
def worklog_upcoming():

    if request.method == 'GET':
        form = UpcomingForm()
        users = User.query.all()
        form.account_id.choices = [(a.id, a.name) for a in users]
        return render_template("worklog/upcoming.html", form = form)

    else:
        upcomingform = UpcomingForm(request.form)

        new = UpcomingWork(upcomingform.account_id.data, upcomingform.name.data, upcomingform.date.data, upcomingform.hours.data)  

        db.session().add(new)
        db.session().commit()

        return redirect(url_for("worklog_list"))

