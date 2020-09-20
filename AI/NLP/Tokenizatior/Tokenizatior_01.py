# 토큰화

# ' 가 안 들어간 tokenizer
from nltk.tokenize import word_tokenize
print(word_tokenize("Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop."))
print(word_tokenize("I'm Violet Cheese, You're so cute.!!!"))

# ' 가 들어간 tokenizer
from nltk.tokenize import WordPunctTokenizer
print(WordPunctTokenizer().tokenize("Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop."))

# 케라스 토큰화 = '를 제외한 나머지 구두점은 제거됨
from tensorflow.keras.preprocessing.text import text_to_word_sequence
print(text_to_word_sequence("Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop."))

# - (하이푼) 단어는 하나로 유지, ' (어포스트로피)는 접어와 분리
from nltk.tokenize import TreebankWordTokenizer
tokenizer = TreebankWordTokenizer()
text="Starting a home-based restaurant may be an ideal. it doesn't have a food chain or restaurant of their own."
print(tokenizer.tokenize(text))