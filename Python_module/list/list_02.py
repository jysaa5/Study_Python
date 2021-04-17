# List & 함수
# list는 함수에 들어가면 주소를 전달하기 때문에 원래 값이 변경된다.
ll = [1, 2, 3, 4, 5]


def change(l):
    l[0] = 1000
    return l


print(change(ll))
print(ll)
