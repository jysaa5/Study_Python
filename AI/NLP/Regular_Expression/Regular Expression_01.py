import re
# . 기호
r = re.compile("a.c")

# 아무런 결과도 출력되지 않는다.
print(r.search("kkk"))

print(r.search("abc"))
