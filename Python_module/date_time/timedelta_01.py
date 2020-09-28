import datetime
from datetime import timedelta

# datetime + datetime.timedelta()
now = datetime.datetime.now()
print(now)
tomorrow = now + datetime.timedelta(days=1)
print(tomorrow)

print('-----------------------------------------------')

# total_seconds()
year = timedelta(days=365)
another_year = timedelta(weeks=40, days=84, hours=23, minutes=50, seconds=600)
print(year==another_year)
print(year.total_seconds())

print('-----------------------------------------------')

# datetime - datetime = timedelta 
oneDatetime = datetime.datetime.strptime('2015-04-15 00:00:00', '%Y-%m-%d %H:%M:%S')
twoDatetime = datetime.datetime.strptime('2015-04-16 00:00:10', '%Y-%m-%d %H:%M:%S')
result = twoDatetime - oneDatetime
print(result)         
print(result.days)    
print(result.seconds) 