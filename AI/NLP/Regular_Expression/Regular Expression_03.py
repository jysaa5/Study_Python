import re
r = re.compile("ab*c")

# 아무런 결과도 출력되지 않는다.
print(r.search("a"))

print(r.search("ac"))

print(r.search("abc"))

print(r.search("abbbbc"))