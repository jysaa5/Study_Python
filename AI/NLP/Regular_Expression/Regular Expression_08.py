import re
r=re.compile("a{2,}bc")

# 아무런 결과도 출력되지 않는다.
print(r.search("bc"))

# 아무런 결과도 출력되지 않는다.
print(r.search("aa"))

print(r.search("aabc"))

print(r.search("aaaaaaaabc"))
