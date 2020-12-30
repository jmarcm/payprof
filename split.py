from datetime import date
day = "2020-12-28"

days = day.split("-")

print(date(int(days[0]), int(days[1]), int(days[2])))
