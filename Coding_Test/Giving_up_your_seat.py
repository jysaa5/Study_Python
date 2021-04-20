# 문제: 문제4 - 자리를 양보해가며!
동물 = ['척추동물', '어류', '척추동물', '무척추동물', '파충류', '척추동물', '어류', '파충류']
'''
1회: ['척추동물'] # False
2회: ['척추동물', '어류'] #False
3회: ['어류', '척추동물'] #HIT
4회: ['어류', '척추동물', '무척추동물'] #False
5회: ['척추동물', '무척추동물', '파충류'] #False
6회: ['무척추동물', '파충류', '척추동물'] #HIT
7회: ['척추동물', '어류', '파충류'] #False
'''

def solution(동물, 자리):
    의자 = []*자리
    answer = 0

    for i in 동물:
        if len(의자)<3:
            if i in 의자:
                히트된페이지 = 의자.pop(의자.index(i))
                의자.append(히트된페이지)
                answer += 1
            else:
                의자.append(i)
                answer += 60
        else:
            if i in 의자:
                히트된페이지 = 의자.pop(의자.index(i))
                의자.append(히트된페이지)
                answer += 1
            else:
                의자.pop(0)
                의자.append(i)
                answer += 60

    return f'{answer//60}분 {answer%60}초'

print(solution(동물, 3))