from app import db
from models import *
from forms import PaySessionForm


course_id = 2

# course = Course.query.filter(Course.id == course_id).first()
# course = Course.query.filter_by(user_id=1).all()

# print(course)

# sessions = Session.query.filter_by(course_id = course_id).all()

# print(sessions)

# for session in sessions:
#     print(session.date)

course = Course.query.get(course_id)
sessions = course.sessions.all()

print(course)
print(sessions)
infos = []
session_info = {}
for session in sessions:
    session_info["session_date"] = session.date
    session_info["session_paid"] = session.paid
    session_info["session_id"] = session.id
    print(session_info)
    infos.append(session_info)

for i in range(len(sessions)):
    print(i)

print(infos)
# entry = [dict(zip(["session.date", "session.paid"], session)) for session in sessions]
# print(entry)


student_info = [("123", "Bob Jones"), ("234", "Peter Jones")]
students = [dict(zip(["student_id", "student_name"], student)) for student in student_info]
print(students) 
# [{'student_id': '123', 'student_name': 'Bob Jones'}, {'student_id': '234', 'student_name': 'Peter Jones'}]