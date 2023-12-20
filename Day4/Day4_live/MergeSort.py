# 합병 정렬

# 리스트를 반으로 나누고 나누고 , 제일 낮은 단위까지 나눔
# 그 작은 리스트 비교해서 정렬
# 그 다음 정렬된 리스트들을 합치면서 또 정렬
# 완성

# 본체 : 정렬된 리스트
def mergesort(lst):
    l = len(lst)

    if l == 1:
        return lst

    mid = l//2
    left = lst[:mid]
    right = lst[mid:]

    left_sorted = mergesort(left)
    right_sorted = mergesort(right)

    return merge(left_sorted, right_sorted)


# 왼쪽 정렬된 리스트 , 오른쪽 정렬된 리스트를 합치는 역할을 하는 함수


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

    # 정렬된 두 리스트를 합치는 내용
    result.extend(left[l:])
    result.extend(right[r:])
    # print(result)
    return result


lst = [8, 7, 5, 10, 3, 1, 4, 2, 6, 13, 76, 43, 1, 3, 12, 45]
print(lst)
print(mergesort(lst))


# 실행
lst = [38, 27, 43, 3, 9, 82, 10]
print(f"원본 리스트: {lst}")
sorted_lst = mergesort(lst)
print(f"정렬 결과: {sorted_lst}")
