# zip(): 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수.
numbers = [1, 2, 3]
letters = ["A", "B", "C"]
for pair in zip(numbers, letters):
    print(pair)

print('--------------------------------')

# index
for i in range(3):
    pair = (numbers[i], letters[i])
    print(pair)
print('--------------------------------')

# 병렬 처리
for number, upper, lower in zip("12345", "ABCDE", "abcde"):
    print(number, upper, lower)
print('--------------------------------')

# unzip
numbers1 = (1, 2, 3)
letters1 = ("A", "B", "C")
pairs = list(zip(numbers1, letters1))
print(pairs)

numbers2, letters2 = zip(*pairs)
print(numbers2)
print(letters2)

print('--------------------------------')
# 사전 변환
keys = [1, 2, 3]
values = ["A", "B", "C"]
print(dict(zip(keys, values)))

print(dict(zip(["year", "month", "date"], [2021, 4, 13])))