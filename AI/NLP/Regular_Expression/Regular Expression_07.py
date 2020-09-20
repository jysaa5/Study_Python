import re
r=re.compile("ab{2,8}c")

# 아무런 결과도 출력되지 않는다.
print(r.search("ac"))

# 아무런 결과도 출력되지 않는다.
print(r.search("abc"))

print(r.search("abbc"))

print(r.search("abbbbbbbbc"))

# 아무런 결과도 출력되지 않는다.
print(r.search("abbbbbbbbbc"))