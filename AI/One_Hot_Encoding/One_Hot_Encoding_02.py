# -*- coding: utf-8 -*-

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import to_categorical

text = "나랑 점심 먹으러 갈래 점심 메뉴는 햄버거 갈래 갈래 햄버거 최고야"

# 정수 인코딩
t = Tokenizer()
t.fit_on_texts([text])
# 각 단어에 대한 인코딩 결과 출력
print(t.word_index)

sub_text = "점심 먹으러 갈래 메뉴는 햄버거 최고야"
encoded = t.texts_to_sequences([sub_text])[0]
print(encoded)

# 원-핫 인코딩 수행
one_hot = to_categorical(encoded)
print(one_hot)