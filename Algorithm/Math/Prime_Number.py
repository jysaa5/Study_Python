# Prime Number (소수)

# solution 1
def isPrime1(N):
    for i in range(2, N):
        if N % i == 0: return False
    return True


# solution 2

def isPrime2(N):
    i = 2
    while i*i <= N:
        if N % i == 0: return False
        i += 1
    return True


number = int(input())
print(isPrime1(number))
print(isPrime2(number))
