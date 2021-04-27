# 문자열 추출(슬라이싱(Slicing))

letters = 'abcdefghijklnmopqrstuvwxyz'

# 문자 1개 추출
print(letters[0])
print(letters[5])
print(letters[25])
print(letters[-1])
print(letters[-2])
print('------------------')


# 원하는 부분 추출
print(letters[0:3])
print('------------------')


# 처음부터 끝까지
print(letters[:])
print('------------------')


# 20번째 문자부터 끝까지
print(letters[20:])
print('------------------')


# 3번재 문자부터 6번째 문자까지
print(letters[3:7])
print('------------------')


# 뒤에서 3번째 문자부터 끝까지
print(letters[-3:])
print('------------------')


# 18번째 문자부터, 뒤에서 4번째 문자까지
print(letters[18:-3])
print('------------------')


# 뒤에서 6번째 문자부터, 뒤에서 3번째 문자까지
print(letters[-6:-2])
print('------------------')


# 0번째 문자 부터 찍고, 7개 이동해서 찍기, 문장 끝까지
print(letters[::7])
print('------------------')


# 4번째 문자부터 찍고, 3개 이동해서 찍기, 20번째 까지 도달
print(letters[4:21:3])
print('------------------')


# 전체 문자열을, 뒤로 1개씩 가면서 찍기
print(letters[::-1])
print('------------------')