# 2447번: 별 찍기 - 10

# solution 1
def get_stars(n):
    matrix = []
    for i in range(3 * len(n)):
        if i // len(n) == 1:
            matrix.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            matrix.append(n[i % len(n)] * 3)
    return(list(matrix))


star = ["***", "* *", "***"]
number = int(input())
e = 0
while number != 3:
    number = int(number / 3)
    e += 1

for i in range(e):
    star = get_stars(star)
    # print(star)
for i in star:
    print(i)
