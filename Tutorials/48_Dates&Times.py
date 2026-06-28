import datetime
# datetime module handles dates, times, and combinations of both

# date object only holds year, month, day, no time info
date = datetime.date(2025, 1, 2)
print(date)            # 2025-01-02
print(date.year)        # 2025
print(date.month)       # 1
print(date.day)         # 2

# today's date, no time
today = datetime.date.today()
print(today)             # current date, e.g. 2026-06-20

# time object only holds hour, minute, second, no date info
time = datetime.time(12, 30, 0)
print(time)               # 12:30:00
print(time.hour)          # 12
print(time.minute)        # 30

# datetime combines date and time together
now = datetime.datetime.now()
print(now)                # current date and time, e.g. 2026-06-20 14:25:09.123456

# strftime() formats a datetime object into a readable string
# %H = hour(24h), %M = minute, %S = second
# %m = month, %d = day, %Y = year(4 digit)
formatted_now = now.strftime("%H:%M:%S %m-%d-%Y")
print(formatted_now)       # e.g. 14:25:09 06-20-2026

# more strftime format examples
print(now.strftime("%A, %B %d, %Y"))   # Saturday, June 20, 2026
print(now.strftime("%I:%M %p"))        # 02:25 PM  (12 hour format with AM/PM)

# strptime() does the opposite, converts a string INTO a datetime object
date_string = "2025-12-25"
parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d")
print(parsed_date)         # 2025-12-25 00:00:00

# comparing two datetime objects directly with < > == 
target_datetime = datetime.datetime(2030, 1, 2, 12, 30, 1)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target date has NOT passed")
# Target date has NOT passed   (2030 hasnt arrived yet)

# timedelta = difference between two datetimes, or used to add/subtract time
difference = target_datetime - current_datetime
print(difference)          # e.g. 1292 days, 9:34:50.123456
print(difference.days)     # just the days part, e.g. 1292

# adding time to a datetime using timedelta
one_week_later = current_datetime + datetime.timedelta(weeks=1)
print(one_week_later)      # current datetime + 7 days

ten_days_ago = current_datetime - datetime.timedelta(days=10)
print(ten_days_ago)        # current datetime - 10 days