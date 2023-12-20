# 퀵 정렬
# 왼쪽 오른쪽이 주어졌을때 피봇을 계산해서
# 피봇보다 작은건 '왼쪽' , 큰 숫자는 '오른쪽'으로 옮긴다

lst = [4, 1, 3, 10, 7, 5, 8]


def lomuto_partition(left, right):
    pivot = lst[right]
    small = left

    for index in range(left, right):
        if lst[index] < pivot:
            lst[small], lst[index] = lst[index], lst[small]
            small += 1
    # 스왑
    lst[small], lst[right] = lst[right], lst[small]

    return small


def lomuto(left, right):
    if left < right:
        pivot_index = lomuto_partition(left, right)
        lomuto(left, pivot_index-1)
        lomuto(pivot_index+1, right)


lomuto(0, len(lst)-1)
print(lst)
