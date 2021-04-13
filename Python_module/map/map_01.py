# map
a = [1.2, 2.5, 3.7, 4.6]
for i in range(len(a)):
    a[i] = int(a[i])

print(a)
print('--------------------------------')

b = [1.2, 2.5, 3.7, 4.6]
b = list(map(int, b))
print(b)

print('--------------------------------')

c = list(map(str, range(10)))
print(c)