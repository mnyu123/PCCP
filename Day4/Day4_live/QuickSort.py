# 퀵 정렬
# 왼쪽 오른쪽이 주어졌을때 피봇을 계산해서
# 피봇보다 작은건 '왼쪽' , 큰 숫자는 '오른쪽'으로 옮긴다

lst = [11, 4, 3, 10, 7, 5, 8]


def lomuto_partition(left, right):
    pivot = lst[right]
    small = left # 위치가 바뀔 인덱스

    for index in range(left, right): # 피봇을 제외한 범위
        if lst[index] < pivot: # 피봇보다 작으면
            lst[small], lst[index] = lst[index], lst[small] # 좌 , 우로 피봇보다 큰거는 오른쪽 작은거는 왼쪽으로 나누는 작업
            small += 1 # 계속 비교를 해야하니까 스몰 이동
    # 스왑
    lst[small], lst[right] = lst[right], lst[small] # 이거는 피봇 

    return small


def lomuto(left, right):
    if left < right:
        pivot_index = lomuto_partition(left, right)
        lomuto(left, pivot_index-1)
        lomuto(pivot_index+1, right)


lomuto(0, len(lst)-1)
print(lst)
