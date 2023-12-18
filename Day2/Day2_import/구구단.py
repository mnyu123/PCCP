# 2차원 리스트를 활용한 구구단 만들기

# [1단, 2단, 3단, 4단, 5단]

# 빈 리스트를 만들어
# 1단 만들어 => 넣어
# 2단 만들어 => 넣어
# 3단 만들어 => 넣어


# 2단 만들기 위해
# 빈 리스트를 만들어
# 21 2 => 넣어
# 22 4 => 넣어
# 23 6 => 넣어
dan_2 = []
for i in range(1, 10):
    dan_2.append(i * 2)

dan_3 = []
for i in range(1, 10):
    dan_3.append(i * 3)

dan_4 = []
for i in range(1, 10):
    dan_4.append(i * 4)


gugudan = []
for k in range(1, 10):
    # k단을 만들어
    dan= []
    for i in range(1, 10):
        dan.append(i * k)
    gugudan.append(dan)

from pprint import pprint
pprint(gugudan)

# 아래 처럼 한줄로 작성이 가능하지만, 좋은 코드는 아님!(이해하기 어려움)
pprint([[i * k for i in range(1, 10)] for k in range(1, 10)])

# 그럼 뭐가 좋은 코드일까?
# (좋은 코드는 사람마다 생각이 다름)

def n_dan(n):
    return [i * n for i in range(1, 10)]
print()
pprint([n_dan(k) for k in range(1, 10)])
