import numpy as np

x = np.arange(12).reshape(3, 4)

print(x.shape)

print(x)

# reshape(-1, 정수)
x = np.arange(12).reshape(-1, 1)
print(x)