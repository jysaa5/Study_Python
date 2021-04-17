text = ['   + -- + - + -   ', '   + --- + - +   ', '   + -- + - + -   ', '   + - + - + - +   ']
print([i for i in text])
print([i for i in range(10) if i % 2 == 0])

# 구구단
# 안에 있는 for문 병렬 관계가 아니다. 두 번째 for문은 첫 번째 for문 안에 속해 있다.
print([f'{i}x{j}={i*j}'for i in range(2, 10) for j in range(1, 10)])