import re
r=re.compile("ab.")

print(r.search("kkkabc"))

# 아무런 결과도 출력되지 않는다.
print(r.match("kkkabc"))

print(r.match("abckkk"))
