# GCD: Greatest Common Divisor

# solution 1
def gcd1(a, b):
    ret = 0
    for i in range(1, min(a, b)+1):
        if i == 0: continue
        if a % i == 0 and b % i == 0: ret = i
    return ret


# solution 2
def gcd2(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i


# solution 3: 유클리드 호제법
def gcd3(a, b):
    return b if a % b == 0 else gcd2(b, a % b)



a, b = map(int, input().split())
print(gcd1(a, b))
print(gcd2(a, b))
print(gcd3(a, b))