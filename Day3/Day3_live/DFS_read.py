# 깊이 우선 탐색 DFS 고찰
# mat = [[0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 1]]
# ----------------------------------------------------------
# mat = [[1, 0, 1, 1, 1, 1],
#        [1, 1, 1, 0, 1, 0],
#        [1, 0, 1, 0, 1, 1],
#        [1, 1, 1, 0, 1, 1]]

# 시작점 : [0,0] 
# 도착점 : [5,3]
# 방문처리는 방문한 길(1)을 0으로 만들어서 처리함

# 스택 현황
# [5,3]
# [4,3],[5,2]
# [4,2]
# [5,0],[4,1]
# [4,0] , [2,2]
# [3,0] , [2,3]
# [2,0] , [1,3]
# [2,1] , [0,3]
# [1,1] , [0,2]
# [0,1]
# [0,0](시작점)