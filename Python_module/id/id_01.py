# list: mutable
# id() 연산자: 변수의 메모리 주소값을 반환함.
a = [1, 2, 3]
print(id(a))

# a의 원소값 변경
a[0] = 5
print(a)

# id 값은 이전과 동일함.
print(id(a))
