# %
test1 = '퍼센트: Hello %s' % 'vio'
print(test1)

test2 = '퍼센트: age: %i' % 12
print(test2)

# format
test3 = 'format: Hello {}'.format('vio')
print(test3)

test4 = 'format: Hello {name}. count: {count}'.format(name='vio', count=5)
print(test4)

# f-string
name = 'vio'
test5 = f'f-string: Hello {name}'
print(test5)

a = 2
b = 3
test6 = f'sum: {a+b}'
print(test6)

test7 = f'Hi {name}'
name = 'vio'
print(test7)

