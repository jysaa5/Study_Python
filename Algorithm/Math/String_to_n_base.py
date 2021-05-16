# 숫자로 구성된 문자열을 N진법에 맞게 변환하기

# solution 1
def stoi1(s, n):
    ret = 0
    l = len(s)
    for i in range(l):
        ret += int(s[i])* n**(l-i-1)
    return ret


# solution 2
def stoi2(s, n):
    ret = 0
    for i in s:
        ret = ret*n + int(i)
    return ret



s, n = input().split()
print(stoi1(s, int(n)))
print(stoi2(s, int(n)))
