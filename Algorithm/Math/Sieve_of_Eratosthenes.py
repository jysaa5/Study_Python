# 소수 판별: 에라토스테네스의 체

def era(N):
    ck, p = [False for _ in range(N+1)], []
    for i in range(2, N+1):
        if ck[i] == True : continue
        p.append(i)
        for j in range(i*i, N+1, i):
            ck[j] = True
    return ck, p


num = int(input())
print(era(num))