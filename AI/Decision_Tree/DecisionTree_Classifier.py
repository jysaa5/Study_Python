from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from elice_utils import EliceUtils

elice_utils = EliceUtils()

"""
1. 데이터를 불러오고,
   학습용 데이터와 테스트용 데이터로 분리하여 
   반환하는 함수를 구현합니다.

   Step01. 사이킷런에 저장된 데이터를 불러옵니다.

   Step02. 불러온 데이터를 
           학습용 데이터(80%)와 테스트용 데이터(20%)로
           분리합니다.

           일관된 결과 확인을 위해 random_state는 
           100으로 설정합니다.
"""


def load_data():
    X, y = None

    train_X, test_X, train_y, test_y = None

    return train_X, test_X, train_y, test_y


"""
2. 분류 의사결정 나무 모델로 
   학습, 예측을 수행한 후 예측 결과를 반환하는 함수를 구현합니다.

   Step01. 분류를 위한 
           의사 결정 나무 모델을 정의합니다.

   Step02. 의사 결정 나무를 
           학습용 데이터에 대해 학습시킵니다.

   Step03. 테스트 데이터에 대한 
           분류 결과를 예측합니다.
"""


def DT_Clf(train_X, train_y, test_X):
    clf = None

    None

    pred = None

    return pred


def main():
    train_X, test_X, train_y, test_y = load_data()

    pred = DT_Clf(train_X, train_y, test_X)
    print('테스트 데이터에 대한 예측 정확도 : {0:.4f}'.format(accuracy_score(test_y, pred)))

    return pred


if __name__ == "__main__":
    main()
