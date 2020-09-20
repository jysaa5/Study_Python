from nltk.tokenize import word_tokenize
text="I am actively looking for Ph.D. students. and you are a Ph.D. student."
print(word_tokenize(text))

from nltk.tag import pos_tag
x = word_tokenize(text)
print(pos_tag(x))