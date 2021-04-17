# mutable한 객체의 변수 간 대입
# shallow copy (얕은 복사)
a = [1, 2, 3]
# b에 a를 할당하면 값이 할당되는 것이 아니라 같은 메모리 주소를 바라본다.
b = a
b[0] = 5
print(a)
print(b)
print(id(a))
print(id(b))
