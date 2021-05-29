# 문제: 11866, 요세푸스 문제 0

from collections import deque

N, K = map(int, input().split())

dq = deque(range(1, N+1))
ans = list()

while len(dq):
    dq.rotate(-K+1)
    ans.append(dq.popleft())

print(f"<{str(ans)[1:-1]}>")