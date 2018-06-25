from flask import render_template, request, redirect, url_for
from flask_login import current_user

from application import app, db, login_required, login_manager
from application.worklog.models import WorkDone
from application.worklog.models import UpcomingWork
from application.auth.models import User
from application.worklog.forms import WorkForm, EditForm, SingleForm, UpcomingForm, UpcomingSingleForm

#Etusivu
@app.route("/worklog", methods=["GET"])
@login_required(role="ANY")
def worklog_stats():

    #Kirjautunut käyttäjä
    u = User.query.get(current_user.id)

    return render_template("worklog/front.html", user=u, total_work=User.total_tasks(), 
                    total_hours=WorkDone.total_hours(), user_hours=WorkDone.user_hours(u),
                    user_work = User.user_tasks(u), upcoming_work = UpcomingWork.select_filtered(u) )

#Yksittäinen työtehtävä
@app.route("/worklog/<work_id>/", methods=["GET"])
@login_required(role="ANY")
def worklog_single(work_id):
    work = WorkDone.query.get(work_id)
    form = SingleForm(obj=work)

    if work.account_id != current_user.id:
        return login_manager.unauthorized()

    return render_template("worklog/single.html", w = WorkDone.query.get(work_id), form=form)

#Listaus
@app.route("/worklog/list", methods=["GET"])
@login_required(role="ANY")
def worklog_list():
    if 'ADMIN' in current_user.roles():
        return render_template("worklog/list.html", worklog = WorkDone.query.all())
    else:    
        return render_template("worklog/list.html", worklog = WorkDone.query.filter_by(account_id = current_user.id) )

#Uuden työtehtävän kirjaussivu
@app.route("/worklog/new")
@login_required(role="ANY")
def worklog_form():
    return render_template("worklog/new.html", form=WorkForm())

#Uuden työtehtävän POST - voisi yhdistää GET:iin, mutta metodien selkeyden vuoksi jätetään tekemättä
@app.route("/worklog/", methods=["POST"])
@login_required(role="ANY")
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
@login_required(role="ANY")
def worklog_edit(work_id):
    work = WorkDone.query.get(work_id)
    form = EditForm(obj=work)

    if work.account_id != current_user.id:
        return login_manager.unauthorized()

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
@login_required(role="ANY")
def worklog_delete(work_id):
    work = WorkDone.query.get(work_id)

    if work.account_id != current_user.id:
        return login_manager.unauthorized()

    db.session().delete(work)
    db.session().commit()

    return redirect(url_for("worklog_list"))

# Alla olevat tulevien työtehtävien routet ovat aika samanlaisia kuin työtehtävienkin routet

@app.route("/worklog/upcoming", methods=["GET"])
@login_required(role="ADMIN")
def worklog_upcoming():
    return render_template("worklog/upcoming/upcoming_list.html", upcoming = UpcomingWork.query.all())


@app.route("/worklog/upcoming/add", methods=["GET", "POST"])
@login_required(role="ADMIN")
def upcoming_new():

    form = UpcomingForm()
    users = User.query.all()
    #Generoi drop downiin käyttäjät
    form.account_id.choices = [(a.id, a.name) for a in users]

    if request.method == 'GET':
        return render_template("worklog/upcoming/upcoming_new.html", form = form)

    else:
        upcomingform = UpcomingForm(request.form)
        #Generoitava käyttäjät ennen validointia, muuten NoneType error!
        upcomingform.account_id.choices = [(a.id, a.name) for a in users]

        #Validoinnin tarkastus
        if not upcomingform.validate():
            return render_template("worklog/upcoming/upcoming_new.html", form = upcomingform)

        new = UpcomingWork(upcomingform.account_id.data, upcomingform.name.data, upcomingform.date.data, upcomingform.hours.data)  

        db.session().add(new)
        db.session().commit()

        return redirect(url_for("worklog_upcoming"))

@app.route("/worklog/upcoming/<id>/delete", methods=["GET", "POST"])
@login_required(role="ADMIN")
def upcoming_delete(id):
    upcoming = UpcomingWork.query.get(id)

    db.session().delete(upcoming)
    db.session().commit()

    return redirect(url_for("worklog_upcoming"))

@app.route("/worklog/upcoming/<id>/")
@login_required(role="ADMIN")
def upcoming_single(id):
    work = UpcomingWork.query.get(id)
    form = UpcomingSingleForm(obj=work)

    return render_template("worklog/upcoming/upcoming_single.html", u = UpcomingWork.query.get(id), form=form)

@app.route("/worklog/upcoming/<id>/edit", methods=["GET", "POST"])
@login_required(role="ADMIN")
def upcoming_edit(id):
    work = UpcomingWork.query.get(id)
    form = UpcomingForm(obj=work)
    users = User.query.all()
    form.account_id.choices = [(a.id, a.name) for a in users]

    if  request.method == 'POST':
        upcomingform = UpcomingForm(request.form)
        upcomingform.account_id.choices = [(a.id, a.name) for a in users]

        #Validoinnin tarkastus
        if not upcomingform.validate():
            return render_template("worklog/upcoming/upcoming_edit.html", u = UpcomingWork.query.get(id), form=upcomingform)

        work.account_id = upcomingform.account_id.data
        work.name = upcomingform.name.data
        work.date = upcomingform.date.data
        work.hours = upcomingform.hours.data

        db.session().commit()

        return redirect(url_for("upcoming_list"))
    else:
        return render_template("worklog/upcoming/upcoming_edit.html", u = UpcomingWork.query.get(id), form=form)


