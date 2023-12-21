from itertools import combinations # 조합 , 순열 순으로 라이브러리를 불러온다.

dic_tennis = {
    '석환': 40,
    '영재': 20,
    '인용': 30,
    '정현': 70,
    '준모': 100
}

dic_pingpong = {
    '석환': 10,
    '영재': 5,
    '인용': 30,
    '정현': 0,
    '준모': 100
}

dic_swim = {
    '석환': 10,
    '영재': 0,
    '인용': 30,
    '정현': 70,
    '준모': 100
}

def solution(dic_tennis, dic_pingpong, dic_swim):
    players = list(dic_tennis.keys())  # 모든 선수의 이름을 리스트로 만듭니다.
    max_ability = 0  # 최대 능력치를 저장할 변수

    # 각 종목별로 선수들의 조합을 만듭니다.
    for comb in combinations(players, 3):
        # 각 조합에서 선수들의 능력치를 합합니다.
        tennis_ability = sum(dic_tennis[player] for player in comb)
        pingpong_ability = sum(dic_pingpong[player] for player in comb)
        swim_ability = sum(dic_swim[player] for player in comb)

        # 각 종목별 능력치 합의 최소값을 구합니다.
        min_ability = min(tennis_ability, pingpong_ability, swim_ability)

        # 최대 능력치를 갱신합니다.
        max_ability = max(max_ability, min_ability)

    return max_ability  # 최대 능력치를 반환합니다.
print(solution(dic_tennis, dic_pingpong, dic_swim))  # 함수 실행 및 결과 출력