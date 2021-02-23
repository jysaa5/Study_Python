import numpy as np


def main():
    print(matrix_tutorial())


def matrix_tutorial():
    A = np.array([[1, 4, 5, 8], [2, 1, 7, 3], [5, 4, 5, 9]])

    # 아래 코드를 작성하세요.
    # 1
    people = np.array([40, 170, 30, 50])
    normalized_people = people / np.sum(people)
    print(normalized_people)

    # 2
    low_var = np.array([1, 0.9, 1.2, 1.5, 0.7, 1.0])
    high_var = np.array([1, 10, 5, -20, 7, 30])
    return 0


if __name__ == "__main__":
    main()