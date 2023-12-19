
from collections import deque

n, m = 4, 6
# 성공 mat
mat = [[1, 0, 1, 1, 1, 1], [1, 1, 1, 0, 1, 0], [1, 0, 1, 0, 1, 1], [1, 1, 1, 0, 1, 1]]

# 실패 mat
# mat = [[1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0], [1, 1, 1, 0, 0, 1]]


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


start_x, start_y = 0, 0
end_x, end_y = n-1, m-1

queue = deque()

queue.append((start_x, start_y))

visited = set()
visited.add((start_x, start_y))


is_success = False
while queue:
    x, y = queue.popleft()

    if (x, y) == (end_x, end_y):
        is_success = True
        break

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if (0<=nx<n) and (0<=ny<m) and (mat[nx][ny] == 1) and ((nx, ny) not in visited):
            queue.append((nx, ny))
            visited.add((nx, ny))
        

print(is_success)