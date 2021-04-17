# list comprehension
# 리스트
print([n*2 for n in range(1, 10+1) if n%2 == 1])
a = [n*2 for n in range(1, 10+1) if n%2 == 1]
print(a)

a = []
for n in range(1, 10+1):
    if n % 2 == 1:
        a.append(n*2)
print(a)

print('-----------------------')

# 딕셔너리
b = {"a": 1, "b": 2}
print({value: key for key, value in b.items()})

a = {}
for key, value in b.items():
    a[value] = key
print(a)

