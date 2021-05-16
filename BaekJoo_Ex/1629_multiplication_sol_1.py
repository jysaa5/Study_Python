# 문제: 1629, 곱셈
# solution 1

def pow_custom(a, b, mod):
    ret = 1
    while b:
        if b % 2 == 1:
            ret = ret * a % mod
        a = a * a % mod
        b //= 2
    return ret


a, b, c = map(int, input().split())

print(pow_custom(a, b, c))