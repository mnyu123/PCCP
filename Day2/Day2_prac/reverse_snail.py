n = 4  # 4x4 달팽이 만드셈

#       오  아  왼  위
nextx = [0, 1, 0, -1]
nexty = [1, 0, -1, 0]

grid = [[0]*n for _ in range(n)]  # 4x4 grid 생성

x = 0  # 시작 좌표 x
y = 0  # 시작 좌표 y
d = 0  # 방향

for num in range(n**2, 0, -1):
    grid[x][y] = num

    # nx , ny -> x,y가 이동을 할 수 있는 후보지
    nx = x + nextx[d]
    ny = y + nexty[d]

    # 어차피 기준은 x , y 좌표 기준으로 움직임
    if nx < 0 or nx >= n or ny < 0 or ny >= n or grid[nx][ny] != 0:
        d = (d + 1) % 4  # 방향 변경
        nx = x + nextx[d]
        ny = y + nexty[d]

    x, y = nx, ny  # nx, ny 위치로 이동

for row in grid:
    print(row)