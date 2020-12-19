import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso

from sklearn.datasets import load_boston


# 1. 사이킷런에 존재하는 데이터를 불러오고, 불러온 데이터를 학습용 데이터와 테스트용 데이터로 분리하여 반환하는 함수를 구현한다.
# Step01. 사이킷런에 존재하는 boston 데이터를 (X, y)의 형태로 불러온다. 
# Step02. 데이터의 변수 이름을 feature_names 에 저장한다.


def load_data():
    X, y = load_boston(return_X_y=True)

    feature_names = load_boston().feature_names

    return X, y, feature_names


# 2. 릿지(Ridge) 회귀를 구현하고, 전체 데이터를 바탕으로 학습시킨 모델을 반환하는 함수를 완성한다.
# Step01. 사이킷런에 구현되어 있는 릿지(Ridge) 회귀 모델을 불러온다.
# 파라미터 alpha를 10으로 설정한다.
# Step02. 불러온 모델을 전체 데이터에 맞춰 학습시킨다.


def Ridge_regression(X, y):
    ridge_reg = Ridge(alpha=10)

    ridge_reg.fit(X, y)

    return ridge_reg


# 2. 라쏘(Lasso) 회귀를 구현하고, 전체 데이터를 바탕으로 학습시킨 모델을 반환하는 함수를 완성한다.
# Step01. 사이킷런에 구현되어 있는 라쏘(Lasso) 회귀 모델을 불러온다.
# 파라미터 alpha를 10으로 설정한다.
# Step02. 불러온 모델을 전체 데이터에 맞춰 학습시킨다.



def Lasso_regression(X, y):
    lasso_reg = Lasso(alpha=10)

    lasso_reg.fit(X, y)

    return lasso_reg


# 각 변수의 beta_i 크기를 시각화하는 함수이다.
def plot_graph(coef, title):
    fig = plt.figure()

    plt.ylim(-1, 1)
    plt.title(title)
    coef.plot(kind='bar')

    plt.savefig("result.png")


def main():
    X, y, feature_names = load_data()

    ridge_reg = Ridge_regression(X, y)
    lasso_reg = Lasso_regression(X, y)

    ## Ridge 회귀의 beta_i의 크기를 저장한다.
    ridge_coef = pd.Series(ridge_reg.coef_, feature_names).sort_values()
    print("Ridge 회귀의 beta_i\n", ridge_coef)

    ## Lasso 회귀의 beta_i의 크기를 저장한다.
    lasso_coef = pd.Series(lasso_reg.coef_, feature_names).sort_values()
    print("Lasso 회귀의 beta_i\n", lasso_coef)

    plot_graph(ridge_coef, 'Ridge')
    plot_graph(lasso_coef, 'Lasso')


if __name__ == "__main__":
    main()