# number, str 등은 함수에 들어가도 값을 전달하기 때문에 원래 값은 변경되지 않는다.
xx = 100


def change(x):
    x += 1000
    return x


print(change(xx))
print(xx)
