# 재귀함수
# 내가 나를 호출하는 방법
# 반복문 <-> 재귀함수

import time

# 1부터 100까지의 합
'''
x = 0
x += 1
x += 2
x += 3
x += 4
...
x += 100
'''
# O(n)
start = time.time() # 시작 시간 저장
x = 0
n = 10000000
for i in range(1, n+1):
    x += i
print(x)
print("time: ", time.time() - start)
print('---------------------------')

# 시그마 공식: n*(n+1)//2
# O(1)
start = time.time() # 시작 시간 저장
x = 0
n = 1000000
x = n*(n+1)//2
print(x)
print("time: ", time.time() - start)
print('---------------------------')

# 합 - 재귀함수
def f(n):
    if n <= 1:
        return 1
    else:
        return n + f(n-1)
n = 100
print(f(n))
print('---------------------------')
'''
    f(n)    n    return     최종
1.  f(100)  100  100+f(99)  100+99+98+..+2+1=5050
2.  f(99)   99   99+f(98)   99+98+97+...+2+1=4950
3.  f(100)  98   98+f(97)   98+97+96+...+2+1=4851
4.  f(100)  97   97+f(96)   97+96+95+...+2+1=4656
5.  f(100)  96   96+f(96)   96+95+94+...+2+1=4753
... f(2)    2    2+f(1)     2+1=3
... f(1)    1    1
'''

# 1부터 100까지의 곱
'''
x = 1
x *= 1
x *= 2
x *= 3
x *= 4
...
x *= 100
'''
# 팩토리얼
# 5! = 5 * 4 * 3 * 2 * 1
x = 1
for i in range(1, 6):
    x *= i
print(x)
print('---------------------------')


def f1(n):
    if n <= 1:
        return 1
    else:
        return n * f1(n-1)
n = 5
print(f1(n))
'''
    f(n)    n    return     최종
1.  f(5)    5    5*f(4)     5*4*3*2*1
2.  f(99)   4    4*f(3)     4*3*2*1
3.  f(100)  3    3*f(2)     3*2*1
4.  f(100)  2    2*f(1)     2*1
5.  f(100)  1    1          1
'''

# 문제 접근 방법
'''
1. 반복문의 경우는 Bottom-up(작은 문제에서 출발)
2. 재귀의 경우는 Top-down(큰 문제에서 출발) -> 재귀 경우는 꼭 종료 조건이 있어야 한다.
'''

# 무한루프
while True:
    if input('##') == 'exit':
        break
    if input('##') == 'hi':
        print('hello world')
    else:
        continue

# 무한루프 - 재귀함수
def console():
    if input('##') == 'exit':
        return None
    if input('##') == 'hi':
        print('hello world')
    console()

console()

# 2진수 구하기 - 반복문
print(bin(11)[2:])
print(oct(11))
print(hex(11))

x = int(input('2진수로 바꿀 숫자를 입력하세요: '))
result = ''
while True:
    if x % 2 == 0:
        result += '0'
    else:
        result += '1'
    x = x // 2
    if x == 1:
        result += str(x)
        print(result[::-1])
        break

'''
   나눈 수  몫    나머지
1. 2       11   1
2. 2       5    1
3. 2       2    0
4.         1    
'''

def 이진수구하기(입력값):
    if 입력값 < 2:
        print(입력값)
    else:
        이진수구하기(입력값//2)
        print(입력값%2)
이진수구하기(11)

def 이진수구하기(입력값):
    if 입력값 < 2:
        return str(입력값)
    else:
        return str(이진수구하기(입력값//2)+str(입력값%2))

print(이진수구하기(11))
'''
이진수구하가(11) -> str(이진수구하기(5)) + str(1) -> 1011
이진수구하기(5)  -> str(이진수구하기(2)) + str(1) -> 101
이진수구하기(2)  -> str(이진수구하기(1)) + str(0) -> 10
이진수구하기(1)  -> 1
'''
# 문자열 뒤집기
def 문자열뒤집기(문자열):
    if 문자열 == '':
        return None
    else:
        문자열뒤집기(문자열[1:]) #앞에 있으면 역순이 되고 뒤로 가면 정순이 된다.
        print(문자열[0])
print(문자열뒤집기('JooYeon'))

def 문자열정순(문자열):
    if 문자열 == '':
        return None
    else:
        print(문자열[0])
        문자열정순(문자열[1:])
print(문자열정순('JooYeon'))

# 문자열 뒤집기 - 반복문
result1 = ''
for i in 'JooYeon':
    result1 = i + result1
print(result1)

result2 = ''
for i in 'JooYeon':
    result2 += i
print(result2)

# 문자열 숫자 덧셈
x = 0
for i in '2231':
    x += int(i)
print(x)


def 문자열숫자합(문자열):
    if 문자열 == '':
        return 0
    else:
        return int(문자열[0]) + int(문자열숫자합(문자열[1:]))

print(문자열숫자합('2231'))


def 숫자세기(숫자):
    if 숫자 <= 0:
        print('끝!!')
    else:
        print(숫자)
        return 숫자세기(숫자-1)

숫자세기(10)


# 피보나치


