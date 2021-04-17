import copy
# copy 모듈의 copy 메서드 또한 얕은 복사이다.
a = [[1, 2], [3, 4]]
b = copy.copy(a)
a[1].append(5)
print(a)
print(b)