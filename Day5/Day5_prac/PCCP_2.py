
# 테니스	탁구	수영
# 석환	40	10	10
# 영재	20	5	0
# 인용	30	30	30
# 정현	70	0	70
# 준모	100	100	100

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

tennis_players = list(dic_tennis.keys())  # 테니스 선수의 이름을 리스트로 만듭니다.
pingpong_players = list(dic_pingpong.keys())  # 탁구 선수의 이름을 리스트로 만듭니다.
swim_players = list(dic_swim.keys())  # 수영 선수의 이름을 리스트로 만듭니다.

tennis_player_ability = list(dic_tennis.values())  # 테니스 선수의 실력을 리스트로 만듭니다.
pingpong_player_ability = list(dic_pingpong.values())  # 탁구 선수의 실력을 리스트로 만듭니다.
swim_player_ability = list(dic_swim.values())  # 수영 선수의 실력을 리스트로 만듭니다.


print("테니스 선수들 이름", tennis_players)
print("탁구 선수들 이름", pingpong_players)
print("수영 선수들 이름", swim_players)

print("테니스 선수들 실력", tennis_player_ability)
print("탁구 선수들 실력", pingpong_player_ability)
print("수영 선수들 실력", swim_player_ability)


tennis_select = ['', '', '']  # 3명의 대표를 뽑아서 저장할 공간
pingpong_select = ['', '', '']  # 3명의 대표를 뽑아서 저장할 공간
swim_select = ['', '', '']  # 3명의 대표를 뽑아서 저장할 공간

tennis_R = len(tennis_select)  # 뽑아야하는 개수
pingpong_R = len(pingpong_select)  # 뽑아야하는 개수
swim_R = len(swim_select)  # 뽑아야하는 개수



max_ability = []  # 최대 실력 모음집

# 테니스 돌리기
def tennis_comb(idx, s_idx):
    if s_idx == tennis_R:  # 출전선수 리스트에 3명 다 뽑으면 4번째 인덱스에 저장하는거 방지
        print("----------------------------------------------------------------------")
        print("테니스만 조합 하나하나의 결과:", select)
        ability = dic_tennis[select[0]] + \
            dic_tennis[select[1]] + dic_tennis[select[2]]
        max_ability.append(ability)
        print("각 조합의 능력치 합:", max_ability)
        print("테니스 최고 능력치 합:", max(max_ability))
        return

    # 각 종목별 끝까지 갔는데 뽑을게 없다면
    # 종료야
    if idx == len(tennis_players):  # 모든 선수를 다 뽑았다면
        return

    if idx == len(pingpong_players):
        return

    if idx == len(swim_players):
        return

    # 현재 선수를 선택합니다.
    tennis_select[s_idx] = tennis_players[idx]
    tennis_comb(idx + 1, s_idx + 1)  # 다음 선수를 뽑습니다.

    # 현재 선수를 선택하지 않습니다.
    tennis_comb(idx + 1, s_idx)  # 다음 선수를 뽑습니다.


tennis_comb(0, 0)  # 조합 생성 시작

# 탁구 돌리기
def pingpong_comb(idx, s_idx):
    if s_idx == pingpong_R:  # 출전선수 리스트에 3명 다 뽑으면 4번째 인덱스에 저장하는거 방지
        print("----------------------------------------------------------------------")
        print("탁구만 조합 하나하나의 결과:", pingpong_select)
        ability = dic_pingpong[pingpong_select[0]] + \
            dic_pingpong[pingpong_select[1]] + dic_pingpong[pingpong_select[2]]
        max_ability.append(ability)
        print("각 조합의 능력치 합:", max_ability)
        print("탁구 최고 능력치 합:", max(max_ability))
        return

    # 각 종목별 끝까지 갔는데 뽑을게 없다면
    # 종료야
    if idx == len(tennis_players):  # 모든 선수를 다 뽑았다면
        return

    if idx == len(pingpong_players):
        return

    if idx == len(swim_players):
        return

    # 현재 선수를 선택합니다.
    pingpong_select[s_idx] = pingpong_players[idx]
    pingpong_comb(idx + 1, s_idx + 1)  # 다음 선수를 뽑습니다.

    # 현재 선수를 선택하지 않습니다.
    pingpong_comb(idx + 1, s_idx)  # 다음 선수를 뽑습니다.

pingpong_comb(0, 0)  # 조합 생성 시작

def swim_comb(idx, s_idx):
    if s_idx == R:  # 출전선수 리스트에 3명 다 뽑으면 4번째 인덱스에 저장하는거 방지
        print("----------------------------------------------------------------------")
        print("수영만 조합 하나하나의 결과:", select)
        ability = dic_swim[select[0]] + \
            dic_swim[select[1]] + dic_swim[select[2]]
        max_ability.append(ability)
        print("각 조합의 능력치 합:", max_ability)
        print("수영 최고 능력치 합:", max(max_ability))
        return

    # 각 종목별 끝까지 갔는데 뽑을게 없다면
    # 종료야
    if idx == len(tennis_players):  # 모든 선수를 다 뽑았다면
        return

    if idx == len(pingpong_players):
        return

    if idx == len(swim_players):
        return

    # 현재 선수를 선택합니다.
    select[s_idx] = swim_players[idx]
    swim_comb(idx + 1, s_idx + 1)  # 다음 선수를 뽑습니다.

    # 현재 선수를 선택하지 않습니다.
    swim_comb(idx + 1, s_idx)  # 다음 선수를 뽑습니다.

swim_comb(0, 0)  # 수영 조합 생성 시작

def solution(ability):
    answer = 0
    return answer