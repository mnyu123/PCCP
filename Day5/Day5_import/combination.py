arr = ['a', 'b', 'c', 'd', 'e']

# 3개를 뽑을꺼야!

select = ['', '', '']


def combination(index, s_index):
    if s_index == len(select):
        print(select)
        return

    if index == len(arr):
        return

    select[s_index] = arr[index]

    # index번째 값을 넣고 다음 자리로 넘어가자
    # [a] 상황에서 [a, b] 만들기
    combination(index + 1, s_index + 1)

    # index번째 값을 넣지 않고 그 자리에 다음 값을 넣을 준비를 하자
    # [a] 상황에서 [b] 만들기
    combination(index + 1, s_index)


combination(0, 0)
