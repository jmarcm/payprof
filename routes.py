from app import app, db, login_manager
from flask import Flask, render_template, request, redirect, url_for, flash
from models import User, Course, Session
from forms import *
from flask_login import current_user, login_user, logout_user, login_required

@app.route("/registration", methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    failed = None
    
    if form.validate_on_submit():
        user = User(username = form.username.data)
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
        print(user)
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index', _external=True))
        else:
            return redirect(url_for("login", _external=True))
    return render_template("login.html", form=form)
    

@app.route("/")
def index():
    return render_template("index.html")



@app.route("/manage")
@login_required
def manage():
    return render_template("manage.html")



# @app.route("/registration-answer")
# def registration_answer():
#     return render_template("registration-answer.html")

@app.route("/settings")
@login_required
def settings():
    return render_template("settings.html")

