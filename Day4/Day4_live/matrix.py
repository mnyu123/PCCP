# 1. 인접행렬 , 인접리스트로 나타나 있는 그래프 사용
# 2. DFS , BFS

# n = 정점의 개수
# m = 간선의 개수
# v = 시작점

# 딕셔너리
from collections import defaultdict, deque
# defaultdict == hashmap (키,값)

from pprint import pprint

n, m, v = map(int, input().split())  # 입력

dic = defaultdict(list)

for _ in range(m):
    s, e = map(int, input().split())
    dic[s].append(e)
    dic[e].append(s)
    print('s와 e는 ', s, e)
pprint(dic)

# dic.items() 는 리스트 형태로 키,값 둘다 들어옴
# 숫자가 작은 순서대로 방문하기 위해서 정렬과정 거침
for key, value in dic.items():
    dic[key] = sorted(value)

# 이제 BFS , DFS 적용

queue = deque()  # 큐 만들고
queue.append(v)  # 초기값 넣고(아마 시작점 말하는듯)

BFS_visited = set()  # 방문기록 저장소
BFS_visited.add(v)  # 바로 초기는 방문기록에 저장

BFS_answer = deque()  # 방문 '순서' 기록용

while queue:
    node = queue.popleft()  # 노드라는 이름으로 v값 씀
    BFS_answer.append(node)

    for next_node in dic[node]:  # 노드(v)가 방문할수있는 모든 곳이
        # 딕셔너리(dic[node])에 저장되어 있음

        if next_node not in BFS_visited:
            # 다음 노드가 방문 안했으면
            queue.append(next_node)  # 거기 지점 큐에 추가
            BFS_visited.add(next_node)  # 그럼 방문 처리


# DFS 방법 시작

stack = deque()
stack.append(v)

DFS_vistied = set()
DFS_vistied.add(v)

DFS_answer = deque()

# while stack:
#     node = stack[-1] # 끝점을 바라본다

#     for next_node in dic[node]:
#         if next_node not in DFS_vistied:
#             stack.append(next_node)
#             DFS_vistied.add(next_node)

#             break
#     else:
#         stack.pop()


# 재귀함수가 있는 DFS 내용
def DFS_func(node):
    DFS_answer.append(node)  # 방문 기록 저장

    for next_node in dic[node]:
        if next_node not in DFS_vistied:
            DFS_vistied.add(next_node)
            DFS_func(next_node)


DFS_func(v)
print("DFS : ", *DFS_answer)
print("BFS : ", *BFS_answer)
# 백준 1260번 문제임