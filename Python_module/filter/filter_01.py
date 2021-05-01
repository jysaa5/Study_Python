# filter
# filter(적용시킬 함수, 적용할 요소들)

# 특정 조건으로 걸러서 걸러진 요소들로 iterator 객체를 만들어서 리턴해준다. 함수의 결과가 참인지 거짓인지에 따라, 해당 요소를 포함할지를 결정한다.
print("filter() :", list(filter(lambda x: x % 2 == 0, [1, 2, 0, 4])))