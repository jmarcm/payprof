from app import db
from models import Session
from datetime import datetime, date

day = "2020-12-28"

days = day.split("-")

# print(date(int(days[0]), int(days[1]), int(days[2])))
# date = datetime(2020, 12, 7)

session = Session(
    date = date(int(days[0]), int(days[1]), int(days[2])),
    course_id = 1
)

db.session.add(session)
db.session.commit()

