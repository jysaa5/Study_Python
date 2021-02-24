import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

X = [8.70153760, 3.90825773, 1.89362433, 3.28730045, 7.39333004, 2.98984649, 2.25757240, 9.84450732, 9.94589513, 5.48321616]
Y = [5.64413093, 3.75876583, 3.87233310, 4.40990425, 6.43845020, 4.02827829, 2.26105955, 7.15768995, 6.29097441, 5.19692852]

beta_0 = 1   # beta_0에 저장된 기울기 값을 조정
beta_1 = 0.5 # beta_1에 저장된 절편 값을 조정

plt.scatter(X, Y) # (x, y) 점을 그린다.
plt.plot([0, 10], [beta_1, 10 * beta_0 + beta_1], c='r') # y = beta_0 * x + beta_1 에 해당하는 선을 그린다.

plt.xlim(0, 10) # 그래프의 X축을 설정
plt.ylim(0, 10) # 그래프의 Y축을 설정

plt.savefig("test_01.png")
