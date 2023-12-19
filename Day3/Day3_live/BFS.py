# 4 6
# 1 0 1 1 1 1
# 1 1 1 0 1 0
# 1 0 1 0 1 1
# 1 1 1 0 1 1

# [[1, 0, 1, 1, 1, 1],
# [1, 1, 1, 0, 1, 0],
# [1, 0, 1, 0, 1, 1],
# [1, 1, 1, 0, 1, 1]]


# BFS -> 너비우선 탐색으로 해결

# ------------------------------------------------------------------
# 너비 우선 탐색(BFS)
# 큐로 구현한다면
# 1. 시작점을 큐에 추가
# 2. 큐에 가장 첫번째 저장된 점을 봄
# 3. 그 점에서 갈 수 있는 "모든 점"을 큐에 추가 , 그리고 방문처리
# 4. 첫번째 저장된 점을 pop
# 5. 2~4번 반복 큐가 빌때까지
# ------------------------------------------------------------------
from collections import deque

n, m = 4, 6

mat = [[1, 0, 1, 1, 1, 1], 
       [1, 1, 1, 0, 1, 0],
       [1, 0, 1, 0, 1, 1], 
       [1, 1, 1, 0, 1, 1]]

# 큐 사용

# 시작점
# 1. 시작점을 큐에 추가
start_x, start_y = 0, 0  # <- 0,0이 시작점임
end_x, end_y = n-1, m-1  # <- 얘는 마지막 지점임
# (왜 -1이냐면 0,1,2,3 이렇게 가서 하나씩 모자라잖아)

queue = deque()  # 사실 큐가 리스트지
queue.append((start_x, start_y))  # 시작점 추가

# 큐 <- 우리가 갈 수 있는 위치의 후보

# 시작점을 큐에 넣고 시작함

# 1-1. 그리고 방문처리 방문한곳에 다시 가지말라고 기록
visited = set()
visited.add((start_x, start_y))

# 예전에 쓰던 4방향 보는거 쓸려고 가져옴
fromx = [0, 0, 1, -1]
fromy = [1, -1, 0, 0]

# 지도 확인
for row in mat:
    print(row)
print(queue)

# 5. 2~4번 반복 큐가 빌때까지
while queue:

    # 1-2. 큐의 제일 첫번째 저장된 점을 본다.
    x, y = queue.popleft()

    # 중간체크
    print("------------------------------------------------------------------")
    print("좌표 확인:", x, ",", y)  # 좌표 상황 확인
    print("------------------------------------------------------------------")
    # 그리고 마지막에 도착지점에 도착한걸 성공하면 알려줌
    if (x, y) == (end_x, end_y):
        print("성공!")

    # 1-3. 그리고 거기서 갈수있는 모든 점(4방향)을
    # 큐에 append(추가하라고) 그리고 거기 방문처리

    # x , y가 갈만한 모든 상하좌우 길 체크함
    for d in range(4):
        nx = x + fromx[d]
        ny = y + fromy[d]
        # +추가 그리드 안에 있는 거만 방문할거라서 제한 둠
        if (0 <= nx) and (nx < n) and (0 <= ny) and (ny < m) and (mat[nx][ny] == 1) and ((nx, ny) not in visited):
            # 제한 내용
            # 1. 길 이여야함(1이여야 한다고) # mat[nx][ny] == 1
            # 2. 방문 안했어야함 # (nx,ny) not in visited

            # 제한 둔거 안에서 방문하려고 후보로 둘거면 큐에 넣을거잖아
            queue.append((nx, ny))
            # 그래서 추가함
            # 그리고 미래를 보고 방문할거라는 예측안으로
            visited.add((nx, ny))
            # 방문기록에 추가함
    print(queue)

    # nx , ny가 갈만한 모든 방향 4방향 후보의 좌표들임

    # 그리고 2~4번 반복
    # ------------------------------------------------------------------
    # 2. 큐에 가장 첫번째 저장된 점을 봄
    # 3. 그 점에서 갈 수 있는 "모든 점"을 큐에 추가 , 그리고 방문처리
    # 4. 첫번째 저장된 점을 pop
    # ------------------------------------------------------------------
