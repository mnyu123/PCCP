# 달팽이 모양으로 숫자 뽑을거임

# 1  2  3  4
# 12 13 14 5
# 11 16 15 6
# 10 9  8  7

# 일케 나와야함

# lst[0][0] = 1 여서 시작함
# 다음건 lst[0][1] = 2 이렇게
# 오른쪽 끝으로 가면 방향바꿈
# 끝날때까지 반복함

# 상 하 좌 우 보게 인덱스를 더해서 거기 체크하게 만들어 둔거

from pprint import pprint

n = 4  # 4x4 달팽이 만드셈

#       오  아  왼  위
nextx = [0, 1, 0, -1]
nexty = [1, 0, -1, 0]

grid = [[0]*n for _ in range(n)]  # 4x4 grid 생성

x = y = 0  # 시작 좌표
d = 0 # 방향

for num in range(1,n**2+1):
    grid[x][y] = num

    # nx , ny -> x,y가 이동을 할 수 있는 후보지
    nx = x + nextx[d]
    ny = y + nexty[d]

    # 어차피 기준은 x , y 좌표 기준으로 움직임
    if nx < 0 or nx >= n or ny < 0 or ny >= n or grid[nx][ny] != 0:
        d = (d + 1) % 4  # 방향 변경
        nx = x + nextx[d]
        ny = y + nexty[d]

    x,y = nx,ny # nx,ny 위치로 이동

for row in grid:
    print(row)