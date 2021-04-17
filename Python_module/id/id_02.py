# set: mutable
# id() 연산자: 변수의 메모리 주소값을 반환함.
x = {1, 2, 3}
print(x)
print(id(x))

# 합집합 연산
x |= {4, 5, 6}
print(x)
print(id(x))