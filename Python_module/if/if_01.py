# if 문
# 기존
v = 1
if v<5:
    print(0)

# ex.1
v = 3
if v < 5: print(0)

# ex.2
v = 3
print(0 if v<5 else 1)

# ex.3
v = 8
print(0 if v<5 else 1)

# 기존
if v<5:
    print(0)
elif v<10:
    print(1)
else:
    print(2)

# ex.1
v = 3
print(0 if v<5 else 1 if v<10 else 2)

v = 8
print(0 if v<5 else 1 if v<10 else 2)

v = 10
print(0 if v<5 else 1 if v<10 else 2)
