# 선택 정렬
# 최소값 기준으로 진행

# 1. 최소값은 가장 왼쪽에 둬야한다.
# 2. 그 위치에 대한 인덱스를 기억한다.
# ex) 최초의 정렬 : index = 0 , 두번째 정렬 : index = 1
# 3. 그 위치에는 가장 작은 값이 들어갈 예정

# 버블정렬처럼 비교하는데 앞 뒤 인덱스 정보 바꾸는게 아니라
# 비교대상인 두개만 바꿈

lst = [4, 1, 3, 10, 7, 5, 8]

for changed_index in range(len(lst)):
    # changed_index = 0
    min_index = changed_index
    for i in range(changed_index, len(lst)):
        if lst[i] < lst[min_index]:
            min_index = i
    # 스왑
    lst[changed_index], lst[min_index] = lst[min_index], lst[changed_index]

    print(lst)
