import datetime as dt

now = dt.datetime.now()
year = now.year
print(type(now))
print(type(year))
print(now.weekday())

birthdate = dt.datetime(year=1989, month=3, day=19, hour=7)
print(birthdate)