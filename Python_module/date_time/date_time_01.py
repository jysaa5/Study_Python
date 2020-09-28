import datetime

# strftime
now = datetime.datetime.now()
print(now)
print('type: ',type(now))

nowDate = now.strftime('%Y-%m-%d')
print(nowDate)
print('type: ',type(nowDate))

nowTime = now.strftime('%H:%M:%S')
print(nowTime)
print('type: ',type(nowTime))

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print(nowDatetime)
print('type: ',type(nowDatetime))

print('----------------------------------------------------------')

# strptime()
myDatetime = datetime.datetime.strptime('2020-09-28 10:07:02', '%Y-%m-%d %H:%M:%S')
print(myDatetime)
print('type: ',type(myDatetime))

print('----------------------------------------------------------')

# replace()
yourDatetime = myDatetime.replace(day=16)
print(myDatetime)
print(yourDatetime)
print('type: ',type(yourDatetime))

print('----------------------------------------------------------')

# combine()
d = datetime.date(2020, 9, 28)
t = datetime.time(12, 23, 38)
dt = datetime.datetime.combine(d, t)
print('combine:',dt)

print('----------------------------------------------------------')

# timetuple()
now = datetime.datetime.now()
nowTuple = now.timetuple()
print(nowTuple)
print(nowTuple.tm_year) 