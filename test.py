# -*- coding: utf8 -*-
from datetime import datetime, timedelta, date

print(datetime.now())
# print("today", date(2020, 12, 7))
datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')

new_time = datetime.strptime("2020-12-28", "%Y-%m-%d")
print("new time", new_time)

"""
Les cours ont lieu le jeudi soir à 18h30
"""

original_date = datetime(2020, 12, 7, 18, 30)
print(original_date)

original_month = original_date.month
print(original_month)

next_date = original_date
# month = original_date.month
month = 1
year = 2021

while True:
    # Action  à exécuter - insertion dans la BDD
    print(next_date)
    next_date += timedelta(days=7)
    if next_date.month > month and next_date.year != year:
        break
