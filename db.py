from app import db
from models import *
from forms import PaySessionForm
from functions import *

user = User.query.get(1)
print(user)

courses = user.courses.all()
# courses = db.relationship("Course", backref="student", lazy="dynamic")
# print(courses)

# total_price = 0
# all_courses_to_pay = {}
# for course in courses:
#     print(course)
#     sessions = course.sessions.filter_by(paid=False).all()
#     all_courses_to_pay[course] = sessions
#     print(sessions)
#     price_to_pay = len(sessions) * course.price
#     print(price_to_pay)
#     total_price += price_to_pay

courses, amount_due = get_user_all_courses_unpaid(1)

print(courses)

for course in courses:
    print(course[0].name)
    print(course[1])
    print(courses[course])