# 개수를 세보자
lst = [1, 5, 6, 7, 2, 3, 6, 8, 1, 6, 8, 4]

counting_lst = [0]*(8+1)

for i in lst:
    counting_lst[i] += 1

# 개수를 셌다
print(counting_lst)

sorted_lst = []

# 단점 : 정수밖에 정렬 못한다
for num, count in enumerate(counting_lst):
    for _ in range(count):
        sorted_lst.append(num)
print(sorted_lst)
