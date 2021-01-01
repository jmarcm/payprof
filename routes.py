from app import app, db, login_manager
from flask import Flask, render_template, request, redirect, url_for, flash
from models import User, Course, Session
from forms import *
from flask_login import current_user, login_user, logout_user, login_required
from functions import *


@app.route("/registration", methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    failed = None

    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.setPassword(form.password.data)
        db.session.add(user)

        failed = False
        try:
            db.session.commit()
        except:
            failed = True

        return render_template("registration-answer.html", failed=failed)

    return render_template("registration.html", form=form)

# user loader


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index', _external=True))
        else:
            return redirect(url_for("login", _external=True))
    return render_template("login.html", form=form, page_name="login")


# manage route
@app.route("/manage")
@login_required
def manage():
    # courses of current user
    courses = Course.query.filter_by(user_id=current_user.get_id()).all()
    return render_template("manage.html", courses=courses)


# course route
@app.route("/course/<int:course_id>", methods=["GET", "POST"])
@login_required
def course(course_id):
    add_form = AddSessionForm()
    update_form = UpdateSessionForm()

    course = Course.query.get(course_id)

    sessions = course.sessions.all()
    db_sessions = set_dict(sessions)

    # calculate the amount due
    sessions_due = [session for session in sessions if not session.paid]
    price_due = '{0:.2f}'.format(len(sessions_due) * course.price)

    # Add (new) entries to form
    if len(update_form.sessions.data) == 0:
        session_info = {}
        for session in sessions:
            session_info["id"] = session.id
            session_info["date"] = session.date
            session_info["paid"] = session.paid
            update_form.sessions.append_entry(session_info)

    # Validation on update_form
    # validate_on_submit() does not work
    if "update" in request.form:
        for updated_session in update_form.sessions.data:

            # set new_session as stored in database
            new_session = db_sessions[int(updated_session["id"])]

            # perform update
            new_session.date = updated_session["date"]
            new_session.paid = updated_session["paid"]

            db.session.commit()

        return redirect(url_for("course", course_id=course_id))

    if add_form.validate_on_submit():
        session = Session(
            date = add_form.date.data,
            paid = add_form.paid.data,
            course_id = course_id
        )
        db.session.add(session)

        try:
            db.session.commit()
            flash("Session added", "add_session")
        except:
            flash("Error, no session added", "add_session")

        return redirect(url_for("course", course_id=course_id))

    return render_template(
        "course.html", add_form=add_form, update_form=update_form, course=course, price_due=price_due
    )


# settings route
@app.route("/settings", methods=["GET", "POST"])
@login_required
def settings():
    form = CourseForm()

    # courses of current user
    courses = Course.query.filter_by(user_id=current_user.get_id()).all()

    if form.validate_on_submit():
        course = Course(
            name=form.name.data,
            meeting_day=form.meeting_day.data,
            meeting_time=form.meeting_time.data,
            price=form.price.data,
            user_id=current_user.get_id()
        )

        db.session.add(course)
        try:
            db.session.commit()
        except Exception:
            print(Exception)

        flash("Course added", "add_course")
        return redirect(url_for("settings"))

    return render_template("settings.html", form=form, courses=courses)


@app.route("/")
def index():
    # courses = Course.query.filter_by(user_id=current_user.get_id()).all()
    courses, amount_due = get_user_all_courses_unpaid(current_user.get_id())
    return render_template("index.html", courses=courses, amount_due=amount_due)
