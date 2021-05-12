# 문제: 1748번, 수 이어쓰기 1

# 1 ~ 9 -> 9 개 * 1
# 10 ~ 99 -> 90 개 * 2
# 100 ~ 999 -> 900 개 * 3
# 1000 ~ 9999 -> 9000개 * 4

# solution 2

n = int(input())
input_len = len(str(n))


def count_number(num, num_len):
    count = 1
    result = 0
    while count <= num_len:
        if count == num_len:
            if count != 1:
                result += ((num - int((count - 1) * '9')) * count)
            else:
                result += num
        else:
            result += count * 9 * (10 ** (count - 1))
        count += 1

    return result


print(count_number(n, input_len))


