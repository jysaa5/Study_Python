# map 함수: 리스트의 요소를 지정된 함수로 처리해주는 함수. map은 원본 리스트를 변경하지 않고 새 리스트를 생성함.
# list(map(함수, 리스트))
# tuple(map(함수, 튜플))

a = [1.2, 2.5, 3.7, 4.6]
for i in range(len(a)):
    a[i] = int(a[i])
print(a)

a = list(map(int, a))
print(a)

a = list(map(str, range(10)))
print(a)