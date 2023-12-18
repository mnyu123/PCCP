[[0, 0, 0, 0],
 [0, 0, 0, 0],
 [0, 0, 0, 0],
 [0, 0, 0, 0],]

grid = []
zero_lst = [0, 0, 0, 0]  # 이 0으로

for _ in range(4):
    grid.append([0, 0, 0, 0])  # 일단 16개의 빈공간 만들어줌
    # print("과정보자", grid)

# print("빈공간 보자! : ", grid)
grid[0][0] = 1

# 지금 결과가 [[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]]
# 이따구로 나오는건 리스트에 [0][0] = 1 반영된놈이 4번 똑같이 나옴
# 즉 , 출력 리스트 다 같은 놈들임

# print("변경된 내용 반영 : ", grid)


# 엘?리먼트로 편하게 또 리스트를 만드는 방법스?
n = 4
grid = [[0]*n for _ in range(n)]

grid[0][0] = 1
grid[0][1] = 2
# 계속 이어서...

num = 1

for i in range(n):
    for j in range(n):
        grid[i][j] = num
        num += 1
print("엘?리먼트 방법 : \n", grid)

for i in range(n):
    for j in range(n):
        grid[i][j] = n * i + 1 + j
        print("과정 보자 : ",grid[i][j])
print("수식 방법 : \n", grid)