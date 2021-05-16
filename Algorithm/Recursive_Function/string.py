# 재귀함수
# 내가 나를 호출하는 방법
# 반복문 <-> 재귀함수
# 문제: 문자열 뒤집기

# 문자열 뒤집기
def reverse_string(input):
    if input == '':
        return None
    else:
        reverse_string(input[1:]) #앞에 있으면 역순이 되고 뒤로 가면 정순이 된다.
        print(input[0])


print(reverse_string('JooYeon'))
print('----------------------------------')


def correct_string(input):
    if input == '':
        return None
    else:
        print(input[0])
        correct_string(input[1:])


print(correct_string('JooYeon'))
print('----------------------------------')


# 문자열 뒤집기 - 반복문
result1 = ''
for i in 'JooYeon':
    result1 = i + result1
print(result1)
print('----------------------------------')

result2 = ''
for i in 'JooYeon':
    result2 += i
print(result2)
print('----------------------------------')

# 문자열 숫자 덧셈
x = 0
for i in '2231':
    x += int(i)
print(x)
print('----------------------------------')


def sum_string_number(input):
    if input == '':
        return 0
    else:
        return int(input[0]) + int(sum_string_number(input[1:]))


print(sum_string_number('2231'))
print('----------------------------------')