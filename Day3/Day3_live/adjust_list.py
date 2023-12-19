# 7 8  # Vertex = 7개, Edge = 8개인 그래프가 있을 때,
# 1 2  # 다음 8개의 줄에 연결 정보를 제공
# 1 3
# 2 4
# 2 5
# 4 6
# 5 6
# 6 7
# 3 7
from pprint import pprint
from collections import defaultdict

# v, e = map(int, input().split())
v, e = 7, 8

# 딕셔너리
dic = defaultdict(list)
for _ in range(e):
    s, e = map(int, input().split())

    dic[s].append(e)
    dic[e].append(s)
pprint("왜 안나옴",dic)
