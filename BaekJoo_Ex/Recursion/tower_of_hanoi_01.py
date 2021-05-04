# 하노이의 탑 이동 순서
# 원판의 개수가 홀수일 때, 1번 원판은 목적 기둥으로 옮긴다.
# 원판의 개수가 짝수일 때, 1번 원판은 목적이 아닌 기둥으로 옮긴다.

k = int(input())
move = []


def hanoi(n, a, b, c):

    if n == 1:
        move.append([a, c])
    else:
        hanoi(n-1, a, c, b) # 맨 마지막 원판을 1 -> 3으로 옮기기 전에 그 전에 있는 원판들이 1 -> 2로 옮겨져 있어야 함
        move.append([a, c]) # 맨 마지막 원판을 1 -> 3 옮기기
        hanoi(n-1, b, a, c) # 나머지 원판을 2 -> 3으로 옮기기


hanoi(k, 1, 2, 3)
print(len(move))
print("\n".join([' '.join(str(i) for i in row) for row in move]))

