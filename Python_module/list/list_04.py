# list slice
a = [1, 2, 3, 4, 6]
print(a[0:2])
print('-----------------')

a = "12345"
print(a[0:2])
print('-----------------')

a = [1, 2, 3, 4, 5]
b = a[:2]
c = a[2:]
print(b)
print(c)
print('-----------------')

# 중첩된 리스트에서 slice
a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(a[2:5])
print(a[3][:2])