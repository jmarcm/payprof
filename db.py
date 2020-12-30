from app import db
from models import *
from forms import PaySessionForm


course_id = 2



course = Course.query.get(course_id)
sessions = course.sessions.all()

# print(course)
# print(sessions)

# calculer le montant des cours restants à payer
to_pay = [session for session in sessions if not session.paid]
price_to_pay = len(to_pay) * course.price
price_to_pay = '{0:.2f}'.format(price_to_pay)
print(to_pay)
print(price_to_pay)