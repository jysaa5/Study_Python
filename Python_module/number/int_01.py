# int(): 클래스

print('int() 클래스')
print(int(1))
print(type(int(1)))
print(int(92233720368547758085555))
print(type(int(92233720368547758085555)))
print(int(1.2))
print(type(int(1.2)))
print('---------------------------')

# 문자열 → 10 진수
print('문자열 → 10 진수')
print(int('1'))
print('---------------------------')

# 진법(base)인자가 함께 전달되었을 경우
print('진법(base)')
print('a', base=16)
print('z', base=36)
print('---------------------------')

# n진수 → 10 진수
print('n진수 → 10 진수')
print(int('0b1011', 2))
print(int('0o13', 8))
print(int('0xb', 16))

