# f-string
# % format, str.format 방법보다 최근

s = 'coffee'
n = 5
result = f'저는 {s}를 좋아합니다. 하루 {n}잔 마셔요.'
print(result)
print('-----------------------------------------')

s1 = 'left'
result1 = f'|{s1:<10}|'
print(result1)
print('-----------------------------------------')

s2 = 'right'
result2 = f'|{s2:>10}|'
print(result2)
print('-----------------------------------------')

s3 = 'mid'
result3 = f'|{s3:^10}|'
print(result3)
print('-----------------------------------------')

# f-string에서 중괄호 출력
num = 10
result4 = f'my age {{{num}}} {{num}}'
print(result4)

# f-string & dict
d = {'name': 'Joo', 'gender': 'female', 'age': 100}
result = f'my name {d["name"]}, gender {d["gender"]}, age{d["age"]}'
print(result)

# f-string & list
n = [100, 200, 300]
print(f'list: {n[0]}, {n[1]}, {n[2]}')

for v in n:
    print(f'list with for: {v}')