mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

mat = []  # 얜 바깥에 있는거

num = 1

lst = []  # 얘는 각각 한줄씩 그거

# lst.append(num) # 빈거에
# num +=1 # 1 더해서 넣으셈  -> lst[1,'','']

# lst.append(num) # 2 들감
# num +=1

# lst.append(num) # 3 들감
# num +=1

n = 4


for _ in range(n):
    lst = []

    # 반복 작업이라 반복문
    for _ in range(n):
        lst.append(num)
        num += 1
    mat.append(lst)

for i in mat:
    print("풀어본 결과 보기", i)

print("------------------------------------------------------------")

mat = []

for i in range(n):
    # 규칙성이
    s = i*4 + 1  # 이거임 0x4+1 , 1x4+1 , 2x4+1 , 3x4+1 임

    lst = list(range(s, s+n))  # 그냥 range로 하면 range(5,9) 일케뜸
    # 앞에 list를 붙여야 똑같이 나옴
    mat.append(lst)
    # range들을 mat에 집어넣겠음

print("다른 결과 보기", mat)
