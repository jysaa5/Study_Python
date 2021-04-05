# range(x): 0부터 x 미만의 숫자를 포함한 range 객체를 만듦
a = range(10)
print(a)

# range(시작 숫자, 끝 숫자)
b = range(1, 11)
print(b)

add = 0
for i in range(1, 11):
    add = add + i
print(add)

marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print('%d번 학생 축하합니다. 합격입니다.' % (number+1))

