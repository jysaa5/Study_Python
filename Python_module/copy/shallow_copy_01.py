# shallow copy (얕은 복사)
a = [1, 2, 3]
# 슬라이싱: 얕은 복사에 해당함.
b = a[:]
print(id(a))
print(id(b))
print(a == b)
print(a is b)

print('-----------')
b[0] = 5
print(a)
print(b)
print(id(a))
print(id(b))

print('-----------')
c = [[1,2], [3, 4]]
d = c[:]
# 다른 주소를 바라보고 있음.
print(id(c))
print(id(d))

# 같은 주소를 바라보고 있음.
print(id(c[0]))
print(id(d[0]))

print('-----------')
# 재할당하는 경우는 문제가 없다. 메모리 주소도 변경된다.
c[0] = [8,9]
print(c)
print(d)
print(id(c[0]))
print(id(d[0]))

print('-----------')
# append를 사용하여 변경하면 d도 변경된다.
c[1].append(5)
print(c)
print(d)
print(id(c[1]))
print(id(d[1]))