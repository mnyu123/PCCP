# 힙 , 큐 이론내용
# 입력 방향 , 출력 방향 다른놈
# 큐가 우선순위에 따라서 뽑고싶음 -> 그게 힙(이진트리)

# 가장 작은 값이 제일 위의 노드
# 가장 작은 값이랑 다음노드 들이랑 자리를 바꿈?
# 리스트를 가지고 '우선순위 큐'를 구현할 수 있음

import heapq

heap = [8, 3, 2, 1, 5, 7, 9]

heapq.heapify(heap)  # 힙으로 만들어줌

print(heap)

heapq.heappush(heap, 4)  # 힙에 4를 추가

print(heap)

print(heapq.heappop(heap))  # 힙에서 가장 작은 값을 뽑아줌
