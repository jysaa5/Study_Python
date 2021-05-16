# 하노이 탑

def hanoi(st, ed, sz):
    if sz == 1:
        return print(st, ed)
    hanoi(st, 6-st-ed, sz-1)
    print(st, ed)
    hanoi(6-st-ed, ed, sz-1)

n = int(input())
if n <= 20:
    print(2**n-1)
    hanoi(1, 3, n)
else:
    print(2**n-1)