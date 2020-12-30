from models import *
from flask_login import current_user

class Courses():

    def get_by_current_user(self):
        """
        docstring
        """
        return Course.query.filter_by(user_id=current_user.get_id()).all()