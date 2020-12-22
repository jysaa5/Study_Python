import numpy as np
from sklearn.manifold import TSNE
from sklearn.datasets import load_wine
import matplotlib.pyplot as plt

# 1. 데이터를 불러오고, 2개의 변수만을 가질 수 있도록 고정하여 반환하는 함수를 구현한다.
# Step01. 사이킷런에 저장된 데이터를 불러온다. 데이터는 (X, y) 형태로 불러와야 한다.
# Step02. column_start로 지정된 특정 column으로부터 연속되는 2개의 변수를 X에 저장한다.
# [실습4]에서 구현한 함수를 그대로 사용할 수 있다.
def load_data():
    X, y = load_wine(return_X_y=True)

    column_start = 6
    X = X[:, column_start: column_start + 2]

    return X



# 2. t-SNE를 활용하여 2차원 데이터를 1차원으로 축소하는 함수를 완성한다.
# Step01. t-SNE의 n_components를 1로 지정하여 tsne를 정의한다.
# Step02. tsne를 활용하여 차원 축소를 진행한 후, 차원이 축소된 데이터 X_tsne를 추출한다.
def tsne_data(X):
    tsne = TSNE(n_components=1)

    X_tsne = tsne.fit_transform(X)

    return tsne, X_tsne


def main():
    X = load_data()

    tsne, X_tsne = tsne_data(X)

    print("- original shape:   ", X.shape)
    print("- transformed shape:", X_tsne.shape)

    print("\n원본 데이터 X :\n", X[:5])
    print("\n차원 축소 이후 데이터 X_tsne\n", X_tsne[:5])


if __name__ == '__main__':
    main()