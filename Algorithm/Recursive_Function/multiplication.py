# 재귀함수
# 내가 나를 호출하는 방법
# 반복문 <-> 재귀함수
# 문제: 곱 구하기

import time

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

# 곱 - 반복문(for)
# 팩토리얼
# 5! = 5 * 4 * 3 * 2 * 1
start = time.time() # 시작 시간 저장
x = 1
for i in range(1, 6):
    x *= i
print(x)
print("time: ", time.time() - start)
print('---------------------------')


# 곱 - 재귀함수
start = time.time() # 시작 시간 저장


def f1(n):
    if n <= 1:
        return 1
    else:
        return n * f1(n-1)


y = 5
print(f1(y))
print("time: ", time.time() - start)
print('---------------------------')
'''
    f(n)    n    return     최종
1.  f(5)    5    5*f(4)     5*4*3*2*1
2.  f(99)   4    4*f(3)     4*3*2*1
3.  f(100)  3    3*f(2)     3*2*1
4.  f(100)  2    2*f(1)     2*1
5.  f(100)  1    1          1
'''