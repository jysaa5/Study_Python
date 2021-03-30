# 10870번: 피보나치 수 5

number = int(input())


def fibonacci_number(n):
    if n == 0:
        return 0
    elif n == 1 or n == 1:
        return 1
    else:
        return fibonacci_number(n-1) + fibonacci_number(n-2)


print(fibonacci_number(number))