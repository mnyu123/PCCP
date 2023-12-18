a = 1
b = '1'
c = True
d = False

#      0  1  2  3  4
lst = [1, 2, 3, 4, 5]

lst[1]  # 2

lst[2] = 100    # [1, 2, 100, 4, 5]

#       key       value
dic = { 'name' : 'jun',
        'age' : 18, 
        'gender' : 'm'
        }

dic['name'] # 'jun


# 반복문

# for
# 1. 컨테이너에서 data를 변수에 반복적으로 할당해서 사용할 때
# 2. 횟수를 반복적으로 활용할 때

# 컨테이너에서 data를 변수에 반복적으로 할당해서 사용할 때

# for i in [1, 2, 3, 4]:
#     # i = 4
#     print(i)

names = ['jun', 'alex', 'ken']

# nums = [0, 1, 2]
nums = range(len(names))

for index in nums:
    print(index+1, '번째 사람', names[index])
print()

num = 1
for name in names:
    print(num, '번째 사람', name)
    num += 1
print()

for index, value in enumerate(names):
    # print(index+1, '번째 사람', value)

    print(f'{index+1}번째 사람 {value}')



# 횟수를 반복적으로 활용할 때
    
for _ in range(5):
    print('안녕!')


# while
# 조건 -> 만족, 만족하지 못했냐
# 조건이 만족하는 한 계속 반복
    # 조건문에 들어가는 변수를 조작하여 언젠가는 조건을 만족하지 않도록 바꿔야 합니다.

# while (condition => boolean(True, False))
    
# while 1<3:

# while 1>3:

# while [1, 2, 3, 4]:

num = 10
while num < 15:

    # 반복 코드를 진행하면서 언젠가는 num<15이 False가 되도록 만들어야 함.
    # ex
    num += 1
    print(num)


# while True:

#     # 어떤 조건을 만족하면 멈춰!
#     if (condition):
#         break
num = 10
while True:
    num += 1
    if num >=15:
        break

# if
# 조건을 만족할 때 실행
    
if True:
    '실행'


if False:
    '실행 안됨'
else:
    '실행됨'



if False:
    '실행 안됨'
elif 1<3:
    '조건에 맞으면 실행 됨'
else:
    '위에가 모두 False일 경우 실행 됨'
    


# 슬라이싱
# list[ 시작점 : 끝점 : step]

#       0   1     2    3    4    5
lst = ['a', 'b', 'c', 'd', 'e', 'f']

print(lst[2:4])
print(lst[0:5:2])

# range
# 0부터 시작하는 수열.
# 슬라이싱과 같은 문법을 공유한다고 생각할 수 있음.
# range(시작점, 끝점, step)

# range(5) => 0, 1, 2, 3, 4
# range(2, 4) => 2, 3