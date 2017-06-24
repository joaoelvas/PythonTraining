import datetime

dt = datetime.datetime.now()

print(dt)

dt_start = dt.replace(hour = 9, minute = 0, second = 0, microsecond = 0)

print(dt_start)


time_worked = datetime.datetime.now() - dt

# time_worked = datetime.timedelta(n_days, n_seconds, n_miliseconds)

# time_worked.days = n_days
# time_worked.seconds = n_seconds
# time_worked.miliseconds = n_miliseconds

now = datetime.datetime.now()

future = now + datetime.timedelta(days=3) # go 3 days ahead

past = now + datetime.timedelta(days=-5) # go back 5 days
# or past = now - datetime.timedelta(days=5)

now.date() # gets date

now.time() # gets time

today = datetime.datetime.today()

today.weekday() # monday = 0, tuesday = 1...

print('Today is: ' + now.strftime('%B %d'))
print('Today is: ' + now.strftime('%m/%d/%Y'))


birthday = datetime.datetime.strptime('2017-08-28', '%Y-%m-%d') # string parsed into time

