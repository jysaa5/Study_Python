from data_plot import *

# 오류가 아닌 경고 메시지 출력 무시
import warnings
warnings.filterwarnings(action='ignore')

import numpy as np
from sklearn.linear_model import LogisticRegression
# 학습용 데이터와 테스트용 데이터 분리
from sklearn.model_selection import train_test_split

# 데이터를 생성하고 반환하는 함수.
def load_data():
    np.random.seed(0)
    # 20: test data, 80: train data
    X = np.random.normal(size=100)
    y = (X > 0).astype(np.float)
    X[X > 0] *= 5
    X += .7 * np.random.normal(size=100)
    X = X[:, np.newaxis]
    # test size: 20%, train size: 80%
    train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.2, random_state=100)
    return train_X, test_X, train_y, test_y

# 1. 로지스틱 회귀 모델을 구현하고, 학습 결과를 확인할 수 있는 main() 함수를 완성.
# Step01. 데이터를 불러온다.
# Step02. 로지스틱 회귀 모델을 정의한다.
# Step03. 학습용 데이터로 로지스틱 회귀 모델을 학습시킨다.
# Step04. 테스트용 데이터로 예측한 분류 결과를 확인한다.

def main():
    train_X, test_X, train_y, test_y = load_data()

    logistic_model = LogisticRegression()

    logistic_model.fit(train_X, train_y)

    predicted = logistic_model.predict(test_X)

    # 예측 결과 확인하기
    print("예측 결과 :", predicted[:10])

    plot_logistic_regression(logistic_model, train_X, train_y)

    return logistic_model


if __name__ == "__main__":
    main()
