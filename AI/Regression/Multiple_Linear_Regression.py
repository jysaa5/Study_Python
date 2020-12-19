import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# boston 데이터를 위한 모듈을 불러온다.
from sklearn.datasets import load_boston


# 1. 사이킷런에 존재하는 데이터를 불러오고, 불러온 데이터를 학습용 데이터와 테스트용 데이터로 분리하여 반환하는 함수를 구현함.
# Step01. 사이킷런에 존재하는 boston 데이터를 (X, y)의 형태로 불러온다..
# Step02. 불러온 데이터를 학습용 데이터와 테스트용 데이터로 분리한다. 학습용 데이터로 전체 데이터의 80%를 사용하고, 테스트용 데이터로 나머지 20%를 사용.
# 동일한 결과 확인을 위하여 random_state를 100으로 설정한다.

def load_data():
    X, y = load_boston(return_X_y = True)

    # shape함수: 데이터프레임내에 있는 row(행)의 개수와 columns(컬럼)의 개수를 반환
    # X.shape -> (행, 열) -> 튜플
    # X.shape[0] -> 행, X.shape[1] -> 열
    print("데이터의 입력값(X)의 개수 :", X.shape[1]) # 컬럼의 개수를 반환

    train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.2, random_state=100)

    return train_X, test_X, train_y, test_y



# 2. 다중 선형회귀 모델을 불러오고, 불러온 모델을 학습용 데이터에 맞추어 학습시킨 후 해당 모델을 반환하는 함수를 구현한다.
# Step01. 사이킷런에 구현되어 있는 다중 선형회귀 모델을 불러온다.
# Step02. 불러온 모델을 학습용 데이터에 맞춰 학습시킨다.


def Multi_Regression(train_X, train_y):
    multilinear = LinearRegression()

    multilinear.fit(train_X, train_y)

    return multilinear


# 3. 모델 학습 및 예측 결과 확인을 위한 main 함수를 완성한다.
# Step01. 학습이 완료된 모델을 활용하여 테스트 데이터에 대한 예측을 수행한다.
# Step02. 사이킷런 회귀 모델 내에 구현되어 있는 score 함수를 사용하여 모델 학습 평가 점수를 model_score 변수에 저장한다.
# Step03. 학습된 모델의 beta_0와 beta_i을 각각 변수 beta_0와 beta_i_list에 저장한다.

def main():
    train_X, test_X, train_y, test_y = load_data()

    multilinear = Multi_Regression(train_X, train_y)

    predicted = multilinear.predict(test_X)

    model_score = multilinear.score(test_X, test_y)

    print("\n> 모델 평가 점수 :", model_score)

    # Y = beta_0 + beta_1 * X_1 + beta_2 * X_2 ... N개
    beta_0 = multilinear.intercept_
    beta_i_list = multilinear.coef_

    print("\n> beta_0 : ", beta_0)
    print("> beta_i_list : ", beta_i_list)

    return predicted, beta_0, beta_i_list, model_score


if __name__ == "__main__":
    main()