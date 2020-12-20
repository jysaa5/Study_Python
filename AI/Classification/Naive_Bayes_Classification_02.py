from sklearn.datasets import load_wine

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# 1. 데이터를 불러오고, 불러온 데이터를 학습용, 테스트용 데이터로 분리하여 반환하는 함수를 구현한다.
# Step01. 사이킷런에 저장되어 있는 데이터를 (X, y) 형태로 불러온다.
# Step02. 불러온 데이터를 학습용 데이터와 테스트용 데이터로 분리한다.
# 학습용 데이터 : 80%, 테스트용 데이터 : 20%, 일관된 결과 확인을 위해 random_state를 0 으로 설정한다.
def load_data():
    X, y = load_wine(return_X_y = True)

    print("데이터 확인해보기 :\n", X[:1])

    train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.2, random_state=0)

    return train_X, test_X, train_y, test_y


# 2. 가우시안 나이브 베이즈 모델을 불러오고, 학습을 진행한 후 테스트 데이터에 대한 예측값을 반환하는 함수를 구현한다.
# Step01. 가우시안 나이브 베이즈 모델을 정의한다.
# Step02. 학습용 데이터에 대해 모델을 학습시킨다.
# Step03. 테스트 데이터에 대한 모델 예측을 수행한다.
def Gaussian_NB(train_X, test_X, train_y, test_y):
    model = GaussianNB()

    model.fit(train_X, train_y)

    predicted = model.predict(test_X)

    return predicted


# 데이터 불러오기, 모델 예측 결과를 확인할 수 있는 함수이다.
def main():
    train_X, test_X, train_y, test_y = load_data()

    predicted = Gaussian_NB(train_X, test_X, train_y, test_y)

    ## 모델 정확도를 통해 분류 성능을 확인해본다.
    print("\nModel Accuracy : ")
    print(accuracy_score(test_y, predicted))


if __name__ == "__main__":
    main()
