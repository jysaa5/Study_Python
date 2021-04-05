# list comprehension(리스트 내포) 사용하기
a = [1, 2, 3, 4]
result1 = []
for num in a:
    result1.append(num*3)

print(result1)

result2 = [num*3 for num in a]
print(result2)

# [표현식 for 항목 in 반복가능객체 if 조건문]
result3 = [num*3 for num in a if num % 2 == 0]
print(result3)

'''
[표현식 for 항목1 in 반복가능객체1 if 조건문1- 
        for 항목2 in 반복가능객체2 if 조건문2
        ...
        for 항목n in 반복가능객체n if 조건문n]
'''

result4 = [x*y for x in range(2, 10)
           for y in range(1, 10)]

print(result4)