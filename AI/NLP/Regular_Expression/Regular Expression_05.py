import re
r = re.compile("^a")

# 아무런 결과도 출력되지 않는다.
print(r.search("bbc"))

print(r.search("ab"))

print(r.search("abbbbc"))

print(r.search("abbbbbbbbc"))