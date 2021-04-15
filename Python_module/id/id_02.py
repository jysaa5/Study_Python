# set
# id() 함수: 메모리 주소를 변수를 구별하기 위한 용도
x = {1, 2, 3}
print(x)
print(id(x))

x |= {4, 5, 6}
print(x)
print(id(x))