import numpy as np

def main():
    A = get_matrix()
    print(A)
    print(matrix_tutorial(A))


# 1
def get_matrix():
    mat = []
    first_row = input()
    n = int(first_row.split(" ")[0])
    m = int(first_row.split(" ")[1])
    for i in range(n):
        row = input()
        mat.append([int(x) for x in row.split(" ")])
    return np.array(mat)


def matrix_tutorial(A):
    # 2
    B = A.T
    print(B)

    # 3
    try:
        C = np.linalg.inv(B)
    except:
        return "not invertible"

    # 4
    return np.sum(C > 0)


if __name__ == "__main__":
    main()