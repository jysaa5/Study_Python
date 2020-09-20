import re

text = "사과 딸기 수박 메론 바나나"

print(re.split(" ",text))

text="""사과
딸기
수박
메론
바나나"""

print(re.split("\n", text))

text="사과+딸기+수박+메론+바나나"
print(re.split("\+",text))