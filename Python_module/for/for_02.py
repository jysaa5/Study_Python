# for 문 1개
list1 = [1, 2, 3, 4, 5]
list2 = []

for i in list1:
    list2.append(i*2)
print(list2)
print([i*2 for i in list1])

# 1차원 list의 각 원소를 한 줄로 출력하기
print('1차원 list의 각 원소를 한 줄로 출력하기')
# ex.1
v = list(range(10))
print(v) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# ex.2
print([i for i in v])
print('Sting join')
print(" ".join(str(i) for i in v))

# for 문 2개
list3 = [1, 2, 3]
for i in list3:
    for j in list3:
        print(i*j, end=" ")
print([i*j for j in list3 for i in list3])

print([i*j if i> 1 else 0 for j in list1 for i in list1])
print([i*j for j in list1  for i in list1 if i> 1])

# 2차원 list의 각 원소를 한 줄로 출력하기
print('2차원 list의 각 원소를 한 줄로 출력하기')
v = [list(range(10)), [10, 11, 12]]
print(v)

for i in v:
    for j in i:
        print(j)

print([j for i in v for j in i])