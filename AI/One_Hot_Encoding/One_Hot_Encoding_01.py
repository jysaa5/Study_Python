# -*- coding: utf-8 -*-
from konlpy.tag import Okt

# KoNLP의 Okt 형태소 분석기 선언 및 생성
okt = Okt()
# 토큰화
token = okt.morphs("나는 자연어 처리를 배운다.")
print(token)

# 고유한 인덱스 부여
word2index={}
for voca in token:
    if voca not in word2index.keys():
        word2index[voca] = len(word2index)
print(word2index)

# 토큰을 입력하면 해당 토큰에 대한 원-핫 벡터를 만들어내는 함수
def one_hot_encoding(word, word2index):
    one_hot_vector = [0]*(len(word2index))
    index = word2index[word]
    one_hot_vector[index] = 1
    return one_hot_vector

print(one_hot_encoding("자연어", word2index))
