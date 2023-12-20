# 본체 -> 정렬된 리스트 return하는 함수
def merge_sort(lst):
    l = len(lst)

    if l == 1:
        return lst

    mid = l//2
    left = lst[:mid]
    right = lst[mid:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)

# 두개를 합치는 녀석
def merge(left, right):
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):

        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    result.extend(left[l:])
    result.extend(right[r:])
    # print(result)
    return result
lst = [8, 7, 5, 10, 3, 1, 4, 2, 6, 13, 76, 43, 1, 3, 12, 45]
print(lst)
print(merge_sort(lst))