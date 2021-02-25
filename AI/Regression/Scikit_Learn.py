import matplotlib as mpl

mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

def loss(x, y, beta_0, beta_1):
    N = len(x)

    x = np.array(x)
    y = np.array(y)
    total_loss = np.sum((y - (beta_0 * x + beta_1)) ** 2)

    return total_loss


X = [8.70153760, 3.90825773, 1.89362433, 3.28730045, 7.39333004, 2.98984649, 2.25757240, 9.84450732, 9.94589513,
     5.48321616]
Y = [5.64413093, 3.75876583, 3.87233310, 4.40990425, 6.43845020, 4.02827829, 2.26105955, 7.15768995, 6.29097441,
     5.19692852]

train_X = np.array(X).reshape(-1, 1)
train_Y = np.array(Y)

'''
모델 트레이닝
'''
lrmodel = LinearRegression()
lrmodel.fit(train_X, train_Y)

'''
loss가 최소가 되는 직선의 기울기와 절편을 계산함
'''
beta_0 = lrmodel.coef_[0]  # lrmodel로 구한 직선의 기울기
beta_1 = lrmodel.intercept_  # lrmodel로 구한 직선의 y절편

print("beta_0: %f" % beta_0)
print("beta_1: %f" % beta_1)
print("Loss: %f" % loss(X, Y, beta_0, beta_1))

plt.scatter(X, Y)  # (x, y) 점
plt.plot([0, 10], [beta_1, 10 * beta_0 + beta_1], c='r')  # y = beta_0 * x + beta_1 에 해당하는 선을 그림.

plt.xlim(0, 10)  # 그래프의 X축을 설정
plt.ylim(0, 10)  # 그래프의 Y축을 설정
plt.savefig("test_03.png")
