# 문제: 나를 먹어요 케이크
# Solution 01: 단순 반복(Iteration)을 통한 해결

def solver(input1, input2, input3):
    minimum = min([input1, input2, input3])
    check_list = []
    num = 0
    while len(check_list) <= minimum:
        possible_range = [num//input1, num//input2, num//input3]
        feasibility = False
        for i in range(0, possible_range[0] + 1):
            for j in range(0, possible_range[1] + 1):
                for k in range(0, possible_range[2] + 1):
                    if input1 * i + input2 * j + input3 * k == num:
                        check_list.append(num)
                        feasibility = True
                        break
                else:
                    continue
                break
            else:
                continue
            break
        if feasibility == False:
            check_list = []
        num += 1
    answer = check_list[0] - 1
    return answer

solution = solver(7, 11, 17)
print(solution)
