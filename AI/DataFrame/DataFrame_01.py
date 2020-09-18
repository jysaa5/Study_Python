import pandas as pd

values = [[1,2,3], [4, 5, 6], [7, 8, 9]]
index = ['one', 'two', 'three']
columns = ['A', 'B', 'C']

df = pd.DataFrame(values, index=index, columns=columns)
print(df)
print("")

print(df.index)
print("")

print(df.columns)
print("")

print(df.values)
print("")

# 데이터 프레임의 생성
# 리스트로 생성하기
data = [
    ['1000', 'Steve', 90.72],
    ['1001', 'James', 78.09],
    ['1002', 'Doyeon', 98.43],
    ['1003', 'Jane', 64.19],
    ['1004', 'Pilwoong', 81.30],
    ['1005', 'Tony', 99.14]
]

df = pd.DataFrame(data)
print(df)
print("")

df = pd.DataFrame(data, columns=['학번', '이름', '점수'])
print(df)
print("")

# 딕셔너리로 생성하기
data = {'학번':['1000', '1001', '1002', '1003', '1004', '1005'],
        '이름':['Steve', 'James', 'Doyeon', 'Jane', 'Pilwoong', 'Tony'],
        '점수': [90.72, 78.09, 98.43, 64.19, 81.30, 99.14]}

df = pd.DataFrame(data)
print(df)
print("")

# 데이터프레임 조회
# 압 부분을 3개만 보기
print(df.head(3))
print("")

# 뒷 부분을 3개만 보기
print(df.tail(3))
print("")

# 학번에 해당되는 열을 보기
print(df['학번'])
print("")

# 외부 데이터 읽기
df = pd.read_csv(r'D:\workspace_Study\AI_Study\NLP_20200812\data.csv')
print(df)
print("")

print(df.index)

