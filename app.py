from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_fontawesome import FontAwesome


# instantiate application
app = Flask(__name__)
app.config['SECRET_KEY'] = "very-confidential-secret"

# instantiate database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///payprof.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

fa = FontAwesome(app)

# create login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

import routes, models