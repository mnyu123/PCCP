# 	테니스	탁구	수영
# 석환	40	10	10
# 영재	20	5	0
# 인용	30	30	30
# 정현	70	0	70
# 준모	100	100	100

from itertools import permutations
# 순열로 풀어야한다.
# 왜냐면 학생들의 순서도 상관이 있기 때문이다.


def solution(ability):
    sport_num = len(ability[0])  # 뽑는 종목의 수
    students_num = len(ability)  # 뽑는 학생의 수
    perms = permutations(range(students_num), sport_num)  # 학생들의 순서를 만들어준다.

    answer = 0  # 최고 능력치 합

    for perm in perms:  # 학생들의 순서를 하나씩 꺼내서
        # 4 , 2 , 3번째 사람이 들어간다고 예시를 둠
        temp = 0  # 능력치 합
        for i in range(sport_num):  # 종목의 수만큼 반복
            temp += ability[perm[i]][i]  # 능력치를 더해준다.
        if temp > answer:  # 능력치 합이 최고 능력치 합보다 크다면
            answer = temp  # 최고 능력치 합을 갱신한다.
    return answer  # 값 반환

print("최고의 합:", solution([[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]))