# 문제: 1748번, 수 이어쓰기 1

# 1 ~ 9 -> 9 개 * 1
# 10 ~ 99 -> 90 개 * 2
# 100 ~ 999 -> 900 개 * 3
# 1000 ~ 9999 -> 9000개 * 4

# solution 1

n = input()
input_len = len(n)


def count_number(num, num_len):
    count = 1
    result = 0
    while count <= num_len:
        if count == num_len:
            if count != 1:
                result += ((int(num) - int((count - 1) * '9')) * count)
            else:
                result += int(num)
        else:
            result += count * 9 * (10 ** (count - 1))
        count += 1

    return result


print(count_number(n, input_len))


