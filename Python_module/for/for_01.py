# for문의 기본 구조
'''
for 변수 in 리스트(튜플, 문자열):
    수행 문장1
    수행 문장2
'''

# 전형적인 for문
number_list = ['one', 'two', 'three']
for i in number_list:
    print(i)

# 다양한 for문의 사용
a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print(first+last)

# for문의 응용
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print('%d번 학생은 합격입니다.' % number)
    else:
        print("%d번 학생은 불합격입니다." % number)

# for문과 continue
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark < 60:
        continue
    print('%d번 학생 축하합니다. 합격입니다. ' % number)
