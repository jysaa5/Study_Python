import pandas as pd

def main():
    # 실제 값
    y_true = pd.Series(
        ["not mafia", "not mafia", "mafia", "not mafia", "mafia",
         "not mafia", "not mafia", "mafia", "not mafia", "not mafia"]
    )
    # 예측된 값
    y_pred = pd.Series(
        ["mafia", "mafia", "not mafia", "not mafia", "mafia",
         "not mafia", "not mafia", "mafia", "not mafia", "not mafia"]
    )

    print("1. 혼동 행렬 :\n", pd.crosstab(y_true, y_pred, rownames=['실제'], colnames=['예측'], margins=True))

# 1. 실행 버튼을 클릭하여, 마피아(mafia)와 시민(not mafia)으로 분류된 혼동 행렬을 확인한다.
# 2. 실행 결과값을 토대로 마피아를 제대로 분석했는 지에 대한 accuracy, precision, recall을 구한다.

    accuracy = (2+5) / 10

    precision = 2/4

    recall = 2/3

    print("\naccuracy : ", accuracy)
    print("precision : ", precision)
    print("recall : ", recall)

    return accuracy, precision, recall


if __name__ == "__main__":
    main()