import time
# print(time.time())

from datetime import date, time, datetime

# print(date(year=2020, month=6, day=6))
# print(time(hour=2, minute=34, second=58))
# print(datetime(year=2020, month=6, day=6, hour=2, minute=34, second=58))

# print(datetime.now())
# print(datetime.today())

# print(repr(date.fromisoformat('2020-06-06')))


date_string = '01-31-2020 14:45:37'
format_string = '%m-%d-%Y %H:%M:%S'
# print(repr(datetime.strptime(date_string, format_string)))


from dateutil import tz
now = datetime.now(tz=tz.tzlocal())
# print(now)
# print(now.tzname())


