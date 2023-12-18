#      0  1  2  3
lst = [1, 2, 3, 4]

print(lst[0]) # 1이 출력

lst[1] = 100  # lst = [1, 100, 3, 4]

lst.append(200)

print(lst)

popped_el = lst.pop()

print(lst)
print(popped_el)

# 구구단 2단을 만들어 보자! [2, 4, 6, 8, 10... 18]

dan_2 = []
for i in range(1, 10):
    # print(2 * i)
    dan_2.append(i * 2)
print(dan_2)

# list comprehension

dan_2 = [i * 2 for i in range(1, 10)]
print(dan_2)


