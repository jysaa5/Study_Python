import matplotlib as mpl

mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    plt.figure(figsize=(5, 5))

    X = []
    Y = []
    N = 1000

    for i in range(N):
        X.append(np.random.rand() * 2 - 1)
        Y.append(np.random.rand() * 2 - 1)
    X = np.array(X)
    Y = np.array(Y)
    distance_from_zero = np.sqrt(X * X + Y * Y)
    is_inside_circle = distance_from_zero <= 1

    print("Estimated pi = %f" % (np.average(is_inside_circle) * 4))

    plt.scatter(X, Y, c=is_inside_circle)
    plt.savefig('circle.png')

if __name__ == "__main__":
    main()