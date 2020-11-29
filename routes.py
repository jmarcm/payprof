from app import app
from flask import render_template
from forms import LoginForm, SettingsForm

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/manage")
def manage():
    return render_template("manage.html")

@app.route("/settings")
def settings():
    return render_template("settings.html")