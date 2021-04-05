print(1, 2, 3)

# sep: print 문의 출력문들 사이에 해당하는 내용을 넣을 수 있음.
# 기본 값으로는 공백이 들어 있으며 이를 사용해 원하는 문자를 입력할 수 있음.
# print((값(변수)), (값(변수))) == print((값(변수), (값(변수)), sep=" ")
print(1, 2, 3, sep="\n")
print('1\n2\n3')

print(1)
print(2)
print(3)

# end: print 문을 이용해 출력을 완료한 뒤의 내용을 수정할 수 있음.
# 기본 값으로는 개행(\n)이 들어가 있으며 이를 사용해 개행을 없애거나 원하는 문자를 입력할 수 있음.
# print(값(변수), end='문자 또는 문자열')
# print(값(변수)) == print(값(변수), end='\n')
print(1, end='')
print(2, end='')
print(3)

print(1, end=' ')
print(2, end=' ')
print(3)


