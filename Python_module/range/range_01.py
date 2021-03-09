
import sys

# range
print(list(range(5)))
print(range(0, 5))
print(type(range(5)))

for i in range(5):
    print(i, end=' ')

a = [n for n in range(1000000)]
print(a)

b = range(1000000)
print(b)
print(type(b))

print(len(a))
print(len(b))
print(len(a) == len(b))

print(sys.getsizeof(a))
print(sys.getsizeof(b))

print(b[999])
