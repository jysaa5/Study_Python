# 11653번: 소인수분해
# solution 1
number = int(input())
i = 2
while number != 1:
    if number % i == 0:
        number = number / i
        print(i)
    else: i += 1