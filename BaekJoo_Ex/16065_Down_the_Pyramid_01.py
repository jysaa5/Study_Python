# 문제: 16065, Down the Pyramid

n = int(input())
input_arr = list(map(int, input().split(" ")))
arr = []
arr.insert(0, 0)
for j in range(1, n+1):
    arr.insert(j, input_arr[j-1])

low = 0
high = 1e18
x = 0

for i in range(n+1):
    x = arr[i] - x
    if i % 2 == 1:
        high = min(high, x)
    else:
        low = max(low, -x)

if low > high or low < 0 or high < 0:
    print(0)
else:
    print(high - low + 1)