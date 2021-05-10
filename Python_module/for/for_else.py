# for ~ else

data = [2, 4, 5, 11, 1]
test = 0

# 변수 사용
for i in data:
    print(i)
    if i > 10:
        test = 1
        print('10보다 큰 수가 있다.')
        break

if test == 0:
    print('10보다 큰 수가 없다.')

# for ~ else 문
for i in data:
    if i > 10:
        print('10보다 큰 수가 있다.')
        break
else:
    print('10보다 큰 수가 없다.')
