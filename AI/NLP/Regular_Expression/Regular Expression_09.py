import re
r=re.compile("[abc]")

# 아무런 결과도 출력되지 않는다.
print(r.search("zzz"))

# 아무런 결과도 출력되지 않는다.
print(r.search("a"))

print(r.search("aaaaaaa"))

print(r.search("baac"))


r = re.compile("[a-z]")
# 아무런 결과도 출력되지 않는다.
print(r.search("AAA"))

print(r.search("aBC"))

# 아무런 결과도 출력되지 않는다.
print(r.search("111"))
