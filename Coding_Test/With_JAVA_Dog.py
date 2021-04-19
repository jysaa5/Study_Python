# 문제: 문제2 - JAVA독과 함께!
돌의내구도 = [1, 2, 1, 4]
독 = [{
    "이름" : "루비독",
    "나이" : "95년생",
    "점프력" : "3",
    "몸무게" : "4",
    },{
    "이름" : "피치독",
    "나이" : "95년생",
    "점프력" : "3",
    "몸무게" : "3",
    },{
    "이름" : "씨-독",
    "나이" : "72년생",
    "점프력" : "2",
    "몸무게" : "1",
    },{
    "이름" : "코볼독",
    "나이" : "59년생",
    "점프력" : "1",
    "몸무게" : "1",
    },
]

# Solution 1
def cross_the_stepping_stone_01(durability, dog):
    # answer = [dog[i]['이름'] for i in range(len(dog))]
    answer = [i['이름'] for i in dog]
    for i in dog:
        dog_position = 0
        while dog_position < len(durability)-1:
            dog_position += int(i['점프력'])
            durability[dog_position-1] -= int(i['몸무게'])
            if durability[dog_position-1]<0:
                answer[answer.index(i['이름'])] = 'fail'
                break;
    return [i for i in answer if i != 'fail']

print(cross_the_stepping_stone_01(돌의내구도.copy(), 독.copy()))

print('---------------------------------------------------------')

# Solution 2
# remove: O(N)
# del: O(1)
def cross_the_stepping_stone_02(durability, dog):
    # answer = [dog[i]['이름'] for i in range(len(dog))]
    answer = [i['이름'] for i in dog]
    for i in dog:
        dog_position = 0
        while dog_position < len(durability)-1:
            dog_position += int(i['점프력'])
            durability[dog_position-1] -= int(i['몸무게'])
            if durability[dog_position-1] < 0:
                del answer[answer.index(i['이름'])]
                break
    return answer

print(cross_the_stepping_stone_02(돌의내구도.copy(), 독.copy()))


print('---------------------------------------------------------')

# Solution 3
# remove: O(N)
# del: O(1)
돌의내구도 = [5, 3, 4, 1, 3, 8, 3]
def cross_the_stepping_stone_03(durability, dog):
    # answer = [dog[i]['이름'] for i in range(len(dog))]
    answer = [i['이름'] for i in dog]
    for i in dog:
        dog_position = 0
        while dog_position < len(durability)-1:
            dog_position += int(i['점프력'])
            durability[dog_position-1] -= int(i['몸무게'])
            if durability[dog_position-1] < 0:
                del answer[answer.index(i['이름'])]
                break
    return answer

print(cross_the_stepping_stone_03(돌의내구도.copy(), 독.copy()))

print('---------------------------------------------------------')

import json
JSON독 = json.dumps(독, ensure_ascii=False)
print(JSON독)
print(JSON독[0])
print(JSON독[:10])
print('----------------------------------------------------------')
JSON독 = json.loads(JSON독)
print(JSON독)
print(JSON독[0])
