from collections import deque

def solution(maps):
    n, m = len(maps),len(maps[0])
    fromx = [0, 0, 1, -1]
    fromy = [1, -1, 0, 0]
    
    start_x, start_y = 0, 0  
    end_x, end_y = n-1, m-1  

    queue = deque() 
    queue.append((start_x, start_y ,1)) 
    
    visited = set()
    visited.add((start_x, start_y))

    while queue:
        x, y , dist = queue.popleft()

        if (x, y) == (end_x, end_y):
            return dist  # 종료 조건을 만족하면 바로 반환

        for d in range(4):
            nx = x + fromx[d]
            ny = y + fromy[d]

            if (0 <= nx < n) and (0 <= ny < m) and (maps[nx][ny] == 1) and ((nx, ny) not in visited):
                queue.append((nx, ny , dist+1))
                visited.add((nx, ny))
    
    return -1  # 경로가 없는 경우 -1 반환