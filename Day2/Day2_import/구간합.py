lst = [3, 56, 78, 1, 3, 5, 6, 78 ,9, 3, 2, 3, 46, 8, 9, 10]

# [3, 56, 78]
# [56, 78, 1]
# [78, 1, 3]
# 길이 3짜리 구간합 중 가장 큰값은??

# sum(lst) : lst의 원소들을 더해서 반환

# 3시 5분 까지 쉬는시간 + 푸는시간



# lst에서 가장 큰값은??
max(lst)

max_num = float('-inf')  # 음의 무한대
max_num = lst[0]

# for num in lst:
#     # num과 max_Num을 비교해서 큰것을 max_num으로 하겟어!
#     # if num < max_num :
#     #     max_num = max_num
#     # if num == max_num :
#     #     max_num = num, max_num

#     if num > max_num :
#         max_num = num



for num in lst:
    if num > max_num :
        max_num = num

lst = [3, 56, 78, 1, 3, 5, 6, 78 ,9, 3, 2, 3, 46, 8, 9, 10]

# 반복을 사용해야할 것 같아요..

max_num = float('-inf')  # 음의 무한대
max_num = lst[0] + lst[1] + lst[2]

for index in range(len(lst) - 2):
    num = lst[index] + lst[index+1] + lst[index+2]

    # num = sum(lst[index : index+2])

    if num > max_num:
        max_num = num

print(max_num)



# 길이 3짜리 구간합을 반복적으로 만드는 것이 아닌, 
# 이전 값을 활용하여 새로운 구간합 생성해서 max값 찾기.

max_num = lst[0] + lst[1] + lst[2]
num = lst[0] + lst[1] + lst[2]

for i in range(len(lst)-3):
    num = num - lst[i] + lst[i+3]
    # num = num - lst[0] + lst[3]
    # num = num - lst[1] + lst[4]
    if num > max_num:
        max_num = num
print(max_num)
# add) list comprehension을 활용하여 길이 3짜리 구간합으로 
# 이루어진 새로운 리스트를 만들고, max값을 취하기

# list comprehension : list의 원소들이 규칙적인 값을 가질 때,
# 이를 활용하여 새로운 리스트를 간편하게 만드는 방법.