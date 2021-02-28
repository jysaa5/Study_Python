def main():
    sensitivity = 0.8
    prior_prob = 0.004
    false_alarm = 0.1

    print("%.2lf%%" % (100 * mammogram_test(sensitivity, prior_prob, false_alarm)))

# A = 1 : 암으로 진단된 경우, B = 1 : 유방암을 가진 경우
def mammogram_test(sensitivity, prior_prob, false_alarm):
    p_a1_b1 = sensitivity  # p(A = 1 | B = 1)

    p_b1 = prior_prob  # p(B = 1)

    p_b0 = 1 - p_b1  # p(B = 0)

    p_a1_b0 = false_alarm  # p(A = 1|B = 0)

    # P(A = 1) = P(A = 1 | B = 0)P(B = 0) * P(A = 1 | B = 1)P(B = 1)
    p_a1 = p_a1_b0 * p_b0 + p_a1_b1 * p_b1  # p(A = 1)

    p_b1_a1 = p_a1_b1 * p_b1 / p_a1  # p(B = 1|A = 1)

    return p_b1_a1


if __name__ == "__main__":
    main()
