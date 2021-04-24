# 문제: 문제7 - Eureka! (문제설명)

cross = [[[3, 0, 1, 1, 8],
		  [5, 0, 4, 5, 4],
	      [1, 5, 0, 5, 1],
	      [1, 2, 1, 0, 1],
		  [0, 2, 5, 1, 1]],
		 [[1, 2, 0, 3, 3],
		  [1, 2, 0, 2, 4],
		  [1, 2, 0, 2, 4],
		  [4, 2, 0, 0, 1],
		  [8, 4, 1, 1, 0]]]

cross_ = cross[0] + cross[1]
print(cross_)
print(cross_[0])
print(cross_[0][4])
print('------------------------')
for i in range(4, -1, -1):
    print(i)
print('------------------------')

for i in range(len(cross_)):
    for j in range(4, -1, -1):
        print(i, j, cross_[i][j])

print('------------------------')

c = [[3, 0, 1, 1, 8],
     [5, 0, 4, 5, 4],
     [1, 5, 0, 5, 1],
     [1, 2, 1, 0, 1],
     [8, 2, 5, 1, 1]]

가중치누적값 = [[0 for i in range(5)] for i in range(5)]
print(가중치누적값)
print('------------------------')

좌표저장 = [[[0,0] for i in range(5)] for j in range(5)]
print(좌표저장)
print('------------------------')

for i in range(5):
    for j in range(5):
        if i == 0 and j == 0:
            가중치누적값[0][0] = c[0][0]
            좌표저장[i][j] = [i, j]
        elif i == 0:
            가중치누적값[i][j] = 가중치누적값[i][j-1] + c[i][j]
            좌표저장[i][j] = [i, j-1]
        elif j == 0:
            가중치누적값[i][j] = 가중치누적값[i-1][j] + c[i][j]
            좌표저장[i][j] = [i-1, j]
        else:
            # 가중치누적값[i][j] = min(가중치누적값[i][j-1], 가중치누적값[i-1][j]) + c[i][j]
            if 가중치누적값[i][j-1] > 가중치누적값[i-1][j]:
                가중치누적값[i][j] = 가중치누적값[i-1][j] + c[i][j]
                좌표저장[i][j] = [i-1, j]
            else:
                가중치누적값[i][j] = 가중치누적값[i][j-1] + c[i][j]
                좌표저장[i][j] = [i, j]


print(c)
print('------------------------')
print(가중치누적값)
print('------------------------')
print(좌표저장)

# Solution 1
가중치누적값 = [[0 for i in range(5)] for i in range(len(cross_))]
좌표저장 = [[[0,0] for i in range(5)] for j in range(len(cross_))]
print('------------------------')
print(가중치누적값)
print('------------------------')
print(좌표저장)
print('------------------------')

for i in range(len(cross_)):
    for j in range(4, -1, -1):
        print(i, j)
        if i == 0 and j == 4:
            가중치누적값[0][4] = cross_[0][4]
            좌표저장[i][j] = [99, 99]
        elif i == 0:
            가중치누적값[i][j] = 가중치누적값[i][j+1] + cross_[i][j]
            좌표저장[i][j] = [i, j+1]
        elif j == 4:
            가중치누적값[i][j] = 가중치누적값[i-1][j] + cross_[i][j]
            좌표저장[i][j] = [i-1, j]
        else:
            가중치누적값[i][j] = 가중치누적값[i][j+1] + cross_[i][j]
            좌표저장[i][j] = [i, j+1]

print(좌표저장)
print('------------------------')
print(좌표저장[len(cross_)-1][0])
print('------------------------')
for k in range(10):
    if k == 0:
        i, j = 좌표저장[len(cross_)-1][0]
    else:
        i, j = 좌표저장[i][j]
    print(i, j)
print('------------------------')
k = 0
while True:
    if k == 0:
        i, j = 좌표저장[len(cross_)-1][0]
    else:
        i, j = 좌표저장[i][j]
    if i == 99 and j == 99:
        break
    k += 1
    print(i, j)
