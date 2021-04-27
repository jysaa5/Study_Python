# 재귀함수
# 내가 나를 호출하는 방법
# 반복문 <-> 재귀함수
# 문제: 2진수 변환


# 2진수 변환 - 파이썬 내장 함수
print(bin(11))
print(bin(11)[2:])
print(oct(11))
print(hex(11))

# 2진수 변환 - 무한루프
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
print('-------------------------------')


def getBinary1(input):
    if input < 2:
        print(input)
    else:
        getBinary1(input // 2)
        print(input % 2)


getBinary1(11)
print('-------------------------------')


def getBinary2(input):
    if input < 2:
        return str(input)
    else:
        return str(getBinary2(input//2)+str(input % 2))


print(getBinary2(11))
print('-------------------------------')

'''
이진수구하가(11) -> str(이진수구하기(5)) + str(1) -> 1011
이진수구하기(5)  -> str(이진수구하기(2)) + str(1) -> 101
이진수구하기(2)  -> str(이진수구하기(1)) + str(0) -> 10
이진수구하기(1)  -> 1
'''