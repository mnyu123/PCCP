# PCCP 코테 수강 1일차 내용 - 자료형 , 변수 등 - Python 버전
print('어 주석 다 했어')
a = 1
b = '1'
c = True
d = False
# 선언과 동시 할당 , 자료형 구분은 느낌?으?로?

# 리스트
list = [1, 2, 3, 4, 5, 6, 7]

list[2]  # 이거 3임
# 알겠지만 0부터 순서대로 가져온다

# 딕셔너리 얘는 (키:값) 으로 가져온다
dic = {'name': 'jun',
       'age': 24,
       'gender': 'M'
       }

dic['name']  # 이거 jun임

# 또복문

# for

# for i in[1,2,3,4,5] :
#     print("또복문",i)

names = ['joe', 'jin', 'max']
# 첫번째 사람 joe , 2번째 사람 jin , 3번째 사람 max

index1 = [0, 1, 2]

index2 = range(len(names))


# # 첫번째 방법
# for i in index1:
#     print(i+1,'번째 사람',names[i])

# # 2번째 방법
# num1 = 1
# for i in index2:
#     print(num1 , '의 사람 ',names[i])
#     num1 +=1
# print()

# # 3번째 방법
# for index1,value in enumerate(names):
#     print(f'{index1+1} enum 사람 {value}')


# while

# 핵전쟁
# temp = 10
# while(temp>0):
#     print(temp)
#     print('발사')
#     temp -=1

# 슬라이싱
# list[시작 : 마지막-1까지]

list1 = ['t', 'e', 's', 't', 'i', 'n', 'g']

# print(list1[2:4]) # 2,3 인덱스
# print(list1[0:7:2]) # 0~7 인덱스인데 2칸씩 건너뜀 0 , 2 , 4, 6


# 기습 문제
lst = [3, 56, 78, 1, 3, 5, 6, 78, 9, 3, 2, 3, 46, 8, 9, 10]
# 3칸씩 짤라서 더했을때 제일 큰거 뭐임

max = 0
max_slice = []


for i in range(len(lst)-2):
    print(lst[i:i+3])
    slice1 = lst[i:i+3]
    sum1 = sum(slice1)

    if (sum1 > max):
        max = sum1  # 제일 큰놈 저장
        max_slice = slice1  # 제일 큰놈 조합

print("제일 큰놈 조합", max_slice)
print("제일 큰놈:", max)
