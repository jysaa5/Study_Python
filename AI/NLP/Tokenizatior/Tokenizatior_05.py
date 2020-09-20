from konlpy.tag import Kkma
kkma=Kkma()
print(kkma.morphs("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))

print(kkma.pos("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))

print(kkma.nouns("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))