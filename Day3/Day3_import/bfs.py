# n, m = map(int,input().split())
# mat = [list(map(int,input().split())) for _ in range(n)]
# 4 6
# 1 0 1 1 1 1
# 1 1 1 0 1 0
# 1 0 1 0 1 1
# 1 1 1 0 1 1

from collections import deque

n, m = 4, 6
# 성공 mat
mat = [[1, 0, 1, 1, 1, 1],
       [1, 1, 1, 0, 1, 0],
       [1, 0, 1, 0, 1, 1],
       [1, 1, 1, 0, 1, 1]]

# 실패 mat
# mat = [[1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0], [1, 1, 1, 0, 0, 1]]


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


start_x, start_y = 0, 0
end_x, end_y = n-1, m-1

# 우리가 갈 수 있는 좌표의 후보지.
queue = deque()

# 시작점을 queue에 append (시작점도 갈 수 있는 후보지. 그중 가장 첫번째로 갈 곳)
queue.append((start_x, start_y))

# 방문했던 곳에 다시 가지 않도록 방문한 좌표를 기록
visited = set()
visited.add((start_x, start_y))

# 반복합니다. # 언제까지? queue가 텅텅 비어있을때 까지
for i in mat:
    print(i)
print(queue)

is_success = False
while queue:
    # queue의 가장 첫번째 저장된 점을 바라봅니다.
    x, y = queue.popleft()

    print(x, y)

    if (x, y) == (end_x, end_y):
        is_success = True
        break

    # 그곳에서 갈 수 있는 모든 점을 queue에 append합니다. 그리고 방문처리 합니다.

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        # 그리드 안에 있는 경우에만! // (nx, ny)가 길이더라! // 방문하지 않았더라!
        if (0 <= nx < n) and (0 <= ny < m) and (mat[nx][ny] == 1) and ((nx, ny) not in visited):

            #  (미래에) 방문을 할 것이다!
            queue.append((nx, ny))
            visited.add((nx, ny))

    print(queue)
    print()

print(is_success)
