# 문제: 1914, 하노이 탑
# st: 시작점, ed: 도착점, sz: 원판 개수
# 6-st-ed: 중간 지점
def hanoi(st, ed, sz):
    if sz == 1:
        return print(st, ed)
    # 마지막 원판 전에 작은 원판들이 중간 기둥에 다 있어야 함
    hanoi(st, 6-st-ed, sz-1)
    # 마지막 원판을 시작점에서 도착점으로 옮김
    print(st, ed)
    # 중간 기둥에 있는 남은 원판을 도착지점으로 옮김
    hanoi(6-st-ed, ed, sz-1)

n = int(input())
print(2 ** n - 1)
if n <= 20:
    hanoi(1, 3, n)