import re
r=re.compile("[^abc]")

# 아무런 결과도 출력되지 않는다.
print(r.search("a"))

# 아무런 결과도 출력되지 않는다.
print(r.search("ab"))

# 아무런 결과도 출력되지 않는다.
print(r.search("b"))

print(r.search("d"))

print(r.search("l"))

print(r.search("5"))

print(r.search("!!"))