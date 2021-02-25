import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import csv

csvreader = csv.reader(open("data/Advertising.csv"))

x = []
y = []

next(csvreader)
for line in csvreader:
    x_i = [float(line[1]), float(line[2]), float(line[3])]
    y_i = float(line[4])
    x.append(x_i)
    y.append(y_i)

X = np.array(x)
Y = np.array(y)

lrmodel = LinearRegression()
lrmodel.fit(X, Y)

beta_0 = lrmodel.coef_[0]  # 0번째 변수에 대한 계수 (페이스북)
beta_1 = lrmodel.coef_[1]  # 1번째 변수에 대한 계수 (TV)
beta_2 = lrmodel.coef_[2]  # 2번째 변수에 대한 계수 (신문)
beta_3 = lrmodel.intercept_  # y절편 (기본 판매량)

print("beta_0: %f" % beta_0)
print("beta_1: %f" % beta_1)
print("beta_2: %f" % beta_2)
print("beta_3: %f" % beta_3)

def expected_sales(fb, tv, newspaper, beta_0, beta_1, beta_2, beta_3):
    sales = beta_0 * fb + beta_1 * tv +beta_2 *newspaper +beta_3
    return sales

print("예상 판매량: %f" % expected_sales(12, 10, 100, beta_0, beta_1, beta_2, beta_3))