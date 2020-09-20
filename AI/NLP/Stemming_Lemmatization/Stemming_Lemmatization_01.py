from nltk.stem import WordNetLemmatizer

n=WordNetLemmatizer()
words=['policy', 'doing', 'organization', 'have', 'going', 'love', 'lives', 'fly', 'dies', 'watched', 'has', 'starting']

print([n.lemmatize(w) for w in words])

print(n.lemmatize('dies', 'v'))

print(n.lemmatize('watched', 'v'))

print(n.lemmatize('has', 'v'))