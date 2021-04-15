# id() 함수: 메모리 주소를 변수를 구별하기 위한 용도
a = [1, 2, 3]
print(id(a))

a[0] = 5
print(a)

a = [5, 2, 3]
print(id(a))