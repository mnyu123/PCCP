# a = int(input('여기에 입력해주세요:'))
# b = int(input('여기에 입력해주세요:'))

lst = [[1, 0, 1, 0, 2],
       [0, 0, 1, 2, 1],
       [0, 1, 0, 1, 2],
       [1, 1, 0, 2, 1],
       [2, 0, 1, 0, 2]
       ]

n, m = 5, 5

count = 0

# 상 하 좌 우 보게 인덱스를 더해서 거기 체크하게 만들어 둔거
nextx = [0, 0, 1, -1]
nexty = [1, -1, 0, 0]

for i in range(n):
    for j in range(m):
        # 아이템이 1인 경우에만 체크할거임
        if lst[i][j] == 1:
            # 2에 근접해 있을때
            for k in range(4):
                # 4방향 다 체크하는 내용임
                nx = i + nextx[k]
                ny = j + nexty[k]
                # 근데 nx,ny 체크 범위가 grid 밖에 나가면 안됨
                if 0 <= nx < n and 0 <= ny < m:
                    # 여기가 이제 2 체크
                    if lst[nx][ny] == 2:
                        count += 1
                        break  # 저 k 반복문 중지
                        # 아무튼 한 방향에 2가 있으면 한번만 세믄됨


# print("2와 근접한 1개수 : ", count)

# 저 코드를 기반으로 2를 기준으로 세는데 , 1을 발견하면 카운트 +1
# 근데 카운트 한놈은 0으로 변경하셈
ncount = 0

for i in range(n):
    for j in range(m):
        # 아이템이 1인 경우에만 체크할거임
        if lst[i][j] == 2:
            # 1에 근접해 있을때
            for k in range(4):
                # 4방향 다 체크하는 내용임
                nx = i + nextx[k]
                ny = j + nexty[k]
                # 근데 nx,ny 체크 범위가 grid 밖에 나가면 안됨
                if (nx < 0) or (nx >= n) or (ny < 0) or (ny >= m):
                    continue
                if lst[nx][ny] == 1:
                    # 여기가 이제 1 체크
                    ncount += 1
                    lst[nx][ny] = 0
                    print("변경된게 맞음?:", lst[nx][ny])
                    # 아무튼 한 방향에 1가 있으면 한번만 세믄됨
for line in lst:
    print(line)
print()


print("2를 기준으로 근접한 1개수 : ", ncount)


# 미친 2차원 배열 이렇게 입력받음 뭔말임
# n , m = map(int,input().split())

# lst = [list(map(int,input().split()))for _ in range(n)]

# print(lst)
