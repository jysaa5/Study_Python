import sklearn.decomposition
import matplotlib.pyplot as plt
import numpy as np
import csv

def main():
    X, attributes = input_data()
    print(X)
    print(X.shape)
    pca_array = normalize(X)
    print(pca_array)
    pca, pca_array = run_PCA(X, 2)
    visualize_2d_wine(pca_array)


def input_data():
    X = []
    attributes = []
    with open("data/attributes.txt") as fp:
        attributes = fp.readlines()
    print(attributes)
    attributes = [x.strip() for x in attributes]
    csvreader = csv.reader(open("data/wine.csv"))

    for line in csvreader:
        float_numbers = [float(x) for x in line]
        X.append(float_numbers)
        print(line)
    return np.array(X), attributes


def run_PCA(X, num_components):
    pca = sklearn.decomposition.PCA(n_components=num_components)
    pca.fit(X)
    pca_array = pca.transform(X)
    return pca, pca_array


def normalize(X):
    for i in range(X.shape[1]):
        X[:, i] = X[:, i] - np.min(X[:, i])
        X[:, i] = X[:, i] / np.max(X[:, i])
    '''
    각각의 feature에 대해,
    178개의 데이터에 나타나는 해당하는 feature의 값이 최소 0, 최대 1이 되도록
    선형적으로 데이터를 이동시킨다.
    '''

    return X


def visualize_2d_wine(X):
    '''X를 시각화하는 코드를 구현합니다.'''
    plt.scatter(X[:, 0], X[:, 1])
    plt.savefig("image.png")


if __name__ == '__main__':
    main()