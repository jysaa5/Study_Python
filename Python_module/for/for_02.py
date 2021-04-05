# for 문 1개
list1 = [1, 2, 3, 4, 5]
list2 = []

for i in list1:
    list2.append(i*2)
print(list2)
print([i*2 for i in list1])


# for 문 2개
list3 = [1, 2, 3]
for i in list3:
    for j in list3:
        print(i*j, end=" ")
print([i*j for j in list3 for i in list3])

print([i*j for j in list3 for i in list3])

print([i*j if i> 1 else 0 for j in list1 for i in list1])
print([i*j for j in list1  for i in list1 if i> 1])