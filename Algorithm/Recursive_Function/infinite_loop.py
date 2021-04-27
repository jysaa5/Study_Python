# 재귀함수
# 내가 나를 호출하는 방법
# 반복문 <-> 재귀함수
# 문제: 무한루프

import time

start = time.time() # 시작 시간 저장
while True:
    if input('##') == 'exit':
        break
    if input('##') == 'hi':
        print('hello world')
    else:
        continue
print("time: ", time.time() - start)
print('---------------------------')

# 무한루프 - 재귀함수
start = time.time() # 시작 시간 저장
def console():
    if input('##') == 'exit':
        return None
    if input('##') == 'hi':
        print('hello world')
    console()


console()
print("time: ", time.time() - start)
print('---------------------------')