import re

text = """이름 : 김철수
전화번호 : 010 - 1234 - 1234
나이 : 30
성별 : 남"""

print(re.findall("\d+" ,text))

print(re.findall("\d+", "문자열입니다."))