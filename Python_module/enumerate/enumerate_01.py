a = [1, 2, 3, 2, 45, 2, 5]
print(a)
print(enumerate(a))
print(list(enumerate(a)))

for i, v in enumerate(a):
    print(i, v)