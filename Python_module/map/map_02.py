# map: 반복 가능한 iterable 객체를 받아서 각 요소에 함수를 적용해주는 함수이다.
a = [1.2, 2.5, 3.7, 4.6]
for i in range(len(a)):
    a[i] = int(a[i])

print(a)
print('--------------------------------')

b = [1.2, 2.5, 3.7, 4.6]
b = list(map(int, b))
print(b)

print('--------------------------------')

c = list(map(str, range(10)))
print(c)