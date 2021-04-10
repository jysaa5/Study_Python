text = ['   + -- + - + -   '
,'   + --- + - +   '
,'   + -- + - + -   '
,'   + - + - + - +   ']

# ord(): 문자 -> 숫자
# chr(): 숫자 -> 문자
l = []
for i in text:
    l.append(chr(int(i.strip().replace(' ', '').replace('+', '1').replace('-', '0'), 2)))

print(''.join(l))
