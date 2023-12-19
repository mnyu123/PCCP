# DFS 재귀함수로

from collections import deque

n, m = 4, 6

mat = [[1, 0, 1, 1, 1, 1],
       [1, 1, 1, 0, 1, 0],
       [1, 0, 1, 0, 1, 1],
       [1, 1, 1, 0, 1, 1]]

# 예전에 쓰던 4방향 보는거 쓸려고 가져옴
fromx = [0, 0, 1, -1]
fromy = [1, -1, 0, 0]

# 시작점
# 1. 시작점을 큐에 추가
start_x, start_y = 0, 0  # <- 0,0이 시작점임
end_x, end_y = n-1, m-1  # <- 얘는 마지막 지점임
# (왜 -1이냐면 0,1,2,3 이렇게 가서 하나씩 모자라잖아)

visited = set()
visited.add((start_x, start_y))

success = False


def DFS(x, y):

    global success # gloabl 붙이면 여기 함수 안에서 저 위에있는
    # success 내용을 변경할 수 있어서 씀

    if (x, y) == (end_x, end_y):
        success = True
        return

     # x , y가 갈만한 모든 상하좌우 길 체크함
    for d in range(4):
        nx = x + fromx[d]
        ny = y + fromy[d]

        if (0 <= nx) and (nx < n) and (0 <= ny) and (ny < m) and (mat[nx][ny] == 1) and ((nx, ny) not in visited):
           visited.add((nx, ny))
           DFS(nx, ny)


DFS(start_x, start_y)
print(success)
