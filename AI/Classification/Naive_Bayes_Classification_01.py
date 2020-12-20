import numpy as np

# 1. "확인" 이라는 키워드가 등장했을 때, 해당 메일이 스팸 메일인지 정상 메일인지 판별하기 위한 함수를 구현한다.

def bayes_theorem():
    # 1. P(“스팸 메일”) 의 확률을 구하기.
    p_spam = 8 / 20

    # 2. P(“확인” | “스팸 메일”) 의 확률을 구하기.
    p_confirm_spam = 5 / 8

    # 3. P(“정상 메일”) 의 확률을 구하기.
    p_ham = 12 / 20

    # 4. P(“확인” | "정상 메일" ) 의 확률을 구하기.
    p_confirm_ham = 2 / 12

    # 5. P( "스팸 메일" | "확인" ) 의 확률을 구하기.
    # P( "스팸 메일" | "확인" ) = P("확인" | "스팸 메일") * P("스팸 메일") / P("확인")
    p_spam_confirm = p_confirm_spam * p_spam / (7 / 20)

    # 6. P( "정상 메일" | "확인" ) 의 확률을 구하기.
    # P( "정상 메일" | "확인" ) =  P("확인" | "정상 메일") * P("정상 메일") / P("확인")
    p_ham_confirm = p_confirm_ham * p_ham / (7 / 20)

    return p_spam_confirm, p_ham_confirm


def main():
    p_spam_confirm, p_ham_confirm = bayes_theorem()

    print("P(spam|confirm) = ", p_spam_confirm, "\nP(ham|confirm) = ", p_ham_confirm, "\n")

    # 두 값을 비교하여 확인 키워드가 스팸에 가까운지 정상 메일에 가까운지 확인한다.
    value = [p_spam_confirm, p_ham_confirm]

    if p_spam_confirm > p_ham_confirm:
        print(round(value[0] * 100, 2), "% 의 확률로 스팸 메일에 가깝습니다.")
    else:
        print(round(value[1] * 100, 2), "% 의 확률로 일반 메일에 가깝습니다.")


if __name__ == "__main__":
    main()
