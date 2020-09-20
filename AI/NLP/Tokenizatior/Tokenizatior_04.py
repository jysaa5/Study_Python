from konlpy.tag import Okt
okt=Okt()
print(okt.morphs("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))

print(okt.pos("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))

print(okt.nouns("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))