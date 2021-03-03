# lambda 인자 : 표현식
print((lambda x, y: x+y)(10, 20))

# map(함수, 리스트)
print(list(map(lambda x: x+10, [1, 2, 3])))
print(list(map(lambda x: x**2, range(5))))

# reduce(함수, 순서형 자료)
from functools import reduce
print(reduce(lambda x, y: x+y, [0, 1, 2, 3, 4]))
print(reduce(lambda x, y: y+x, 'abcde'))

# filter(함수, 리스트)
print(list(filter(lambda x:x<5, range(10))))