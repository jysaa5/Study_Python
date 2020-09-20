# Matplotlib
import matplotlib.pyplot as plt

# 라인 플롯 그리기
plt.title('test')
plt.plot([1, 2, 3, 4], [2, 4, 8, 6])
plt.show()

# 축 레이블 삽입하기
plt.title('test')
plt.plot([1, 2, 3, 4], [2, 4, 8, 6])
plt.xlabel('hours')
plt.ylabel('score')
plt.show()

# 라인 추가와 범례 삽입하기
plt.title('students')
plt.plot([1, 2, 3, 4], [2, 4, 8, 6])
plt.plot([1.5, 2.5, 3.5, 4.5],[3, 5, 8, 10])
plt.xlabel('hours')
plt.ylabel('score')
plt.legend(['A student', 'B student'])
plt.show()