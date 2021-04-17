# list Indexing
a = [1, 2, 3]
print(a)
print(a[0])
print(a[0]+a[2])
print(a[-1])

print('----------------------------')
# 이중 리스트
a = [1, 2, 3, ['a', 'b', 'c']]
print(a[0])
print(a[-1])
print(a[3])
print(a[-1][0])
print(a[-1][1])
print(a[-1][2])

print('----------------------------')
# 삼중 리스트
a = [1, 2, ['a', 'b', ['Life', 'is']]]
print(a[2][2][0])
