# 정렬

lst1 = [1, 54, 7, 4, 76, 89, 2]

# sort() 메소드
result1 = lst1.sort()
print(lst1, result1)
# 리스트 1은 정렬됨 , 자기자신이 정렬되는 상태
# 근데 결과값은 없는 상태임

lst2 = [1, 54, 7, 4, 76, 89, 2]

# sorted() 함수
result2 = sorted(lst2)
print(lst2, result2)
# 리스트 2는 처음거 내용 유지하는데
# sorted함수 거치면서 결과값에 정렬된 데이터로 반환함

# 키
# 정렬의 기준을 잡기위한 파라미터

lst3 = [[2, 7], [1, 5], [3, 1]]


def order(x):
    return x[1]


# 앞에 있는 숫자 순서대로 정렬
print(sorted(lst3))

# order 함수로 뒤에있는 숫자[7,5,1] 을 기준으로 정렬시키기
print(sorted(lst3, key=order))

# 람다식
print(sorted(lst3, key=lambda x: x[1]))

# 람다식 변형
print(sorted(lst3 , key=lambda x: -max(x)))