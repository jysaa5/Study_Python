# 문제: 문자 해독
text = ['   + -- + - + -   ', '   + --- + - +   ', '   + -- + - + -   ', '   + - + - + - +   ']

# ord(): 문자 -> 숫자
# chr(): 숫자 -> 문자

# Solution 1
l = []
for i in text:
    l.append(chr(int(i.strip().replace(' ', '').replace('+', '1').replace('-', '0'), 2)))

print(''.join(l))

# Solution 2
print(''.join([chr(int(i.strip().replace(' ', '').replace('+', '1').replace('-', '0'), 2)) for i in text]))

# map
# zip
# Solution 3
s = [i.strip().replace(' ', '').replace('+', '1').replace('-', '0') for i in text]
print(s)
print(''.join(list(map(lambda x: chr(int(x,2)),s))))


# Solution 4
def f(x):
    return chr(int(x, 2))

print(''.join(list(map(f,s))))
