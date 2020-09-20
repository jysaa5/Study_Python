import re
r=re.compile("ab{2}c")

# 아무런 결과도 출력되지 않는다.
print(r.search("ac"))

# 아무런 결과도 출력되지 않는다.
print(r.search("abc"))

print(r.search("abbc"))

# 아무런 결과도 출력되지 않는다.
print(r.search("abbbbbc"))