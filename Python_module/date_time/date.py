from datetime import date

a = date(2020, 9, 28).weekday()
print('월:0, 화:1, 수:2, 목:3, 금:4, 토:5, 일:6 →',a)

b = date(2020, 9, 28).isoweekday()
print('월:1, 화:2, 수:3, 목:4, 금:5, 토:6, 일:7 →', b)