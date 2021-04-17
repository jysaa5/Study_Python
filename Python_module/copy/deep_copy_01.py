# 깊은 복사: 내부에 객체들끼리 모두 새롭게 copy 되는 것
import copy
a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
a[1].append(5)
print(a)
print(b)