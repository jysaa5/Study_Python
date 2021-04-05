# if condition에 해당하는 값만 출력하기
v = list(range(10, 20))
print(v)

# 기존
for i in v:
    if i==12:
        print(i)

# 한 줄로
[i for i in v if i==12]


for i in v:
    if i==12:
        print(i)
    else:
        print('No')

[i if i==12 else "No" for i in v]