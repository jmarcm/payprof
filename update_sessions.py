from app import db
import datetime
from models import Session, Course
from functions import set_dict

course_id = 2
course = Course.query.get(course_id)
db_sessions = course.sessions.all()
# print(db_sessions)


dbd_sessions = set_dict(db_sessions)

# print(dbd_sessions)

data = [{'id': 14, 'date': datetime.date(2020, 11, 3), 'paid': True, 'csrf_token': None}, {'id': 15, 'date': datetime.date(2020, 11, 7), 'paid': False, 'csrf_token': None}, {'id': 16, 'date': datetime.date(2020, 11, 10), 'paid': False, 'csrf_token': None}, {'id': 17, 'date': datetime.date(2020, 11, 17), 'paid': True, 'csrf_token': None}, {'id': 18, 'date': datetime.date(2020, 11, 24), 'paid': False, 'csrf_token': None}, {'id': 19, 'date': datetime.date(
    2020, 10, 31), 'paid': True, 'csrf_token': None}, {'id': 20, 'date': datetime.date(2020, 12, 1), 'paid': False, 'csrf_token': None}, {'id': 21, 'date': datetime.date(2020, 12, 8), 'paid': True, 'csrf_token': None}, {'id': 22, 'date': datetime.date(2020, 12, 15), 'paid': False, 'csrf_token': None}, {'id': 23, 'date': datetime.date(2020, 10, 20), 'paid': True, 'csrf_token': None}, {'id': 24, 'date': datetime.date(2020, 10, 15), 'paid': True, 'csrf_token': None}]

for updated_session in data:
    print(updated_session["date"])
    new_session = dbd_sessions[updated_session["id"]]
    new_session.date = updated_session["date"]
    new_session.paid = updated_session["paid"]
    print(new_session)
    print(new_session.paid)
    # db.session.commit()