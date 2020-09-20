import re
text = """100 John    PROF
101 James   STUD
102 Mac   STUD"""

# \s+ 최소 공백 1개이상의 패턴
print(re.split('\s+', text))

# \d 숫자가 최소 1개 이상의 패턴
print(re.findall('\d+',text))

# 대문자 찾기
print(re.findall('[A-Z]',text))

# 대문자 4번 반복 찾기
print(re.findall('[A-Z]{4}',text))

# 대문자, 소문자 찾기
print(re.findall('[A-Z][a-z]+',text))

# 알파벳이 아닌것은 공백으로 처리
letters_only = re.sub('[^a-zA-Z]', ' ', text)

print(letters_only)