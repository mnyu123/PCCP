# 3번 문제 해설
# 내 종자 상태를 알고싶으면 부모의 상태를 먼저 알아야함

# 중요한점은 내가 부모와 어떻게 '연관' 되어있나 생각해봐야함


def solution(queries):
    answer = []
    for generation, order in queries:
        # 답변에 추가함 저 함수 돌린 결과를
        answer.append(get_genes(generation, order))
    return answer

# 유전자 형이 무엇인지를 알려주는 함수
# generation은 내 세대를 말함
# order는 내가 몇번째인지를 말함


def get_genes(generation, order):
    # 1세대는 무조건 Rr
    if generation == 1:
        return 'Rr'

    # 규칙성

    # 1세대 2세대 3세대  4세대
    # 0123 4567 891011 12131415

    # 이럴때 보면 4로 나누고 몫에 1을 더하면 부모가 몇세대인지 알 수있음
    # 이 내용으로 밑에 한줄식 parent_order를 만든거임

    parent_order = (((order-1)//4) + 1)  # 나의 부모의 위치를 알 수있음

    # 부모의 유전자형을 알 수 있는 내용
    # generation-1 이게 윗 세대를 말함(부모면 부모의 부모 느낌스)
    parent = get_genes(generation-1, parent_order)

    if parent == 'RR' or parent == 'rr':
        return parent

    # parent가 Rr 인 경우
    if order % 4 == 0:
        return 'rr'
    elif order % 4 == 1:
        return 'RR'
    else:
        return 'Rr'
