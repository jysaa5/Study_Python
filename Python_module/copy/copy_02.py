# immutable한 객체의 변수 간 대입

a = 'abc'
b = a
print(a)
print(b)
print(id(a))
print(id(b))

print('---------------')

# b에 다른 값을 할당하면 재할당이 이루어지며 메모리 주소가 변경된다.
b = "abcd"
print(a)
print(b)
print(id(a))
print(id(b))
