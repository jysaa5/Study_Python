# str: immutable
# id() 연산자: 변수의 메모리 주소값을 반환함.
s = 'abc'
print(s)
print(id(s))
print(s[0])
# s변수 첫번째 글자 변경을 시도하면 에러가 발생한다.
# 다른 값을 할당
s = 'def'
print(s)
print(id(s))
