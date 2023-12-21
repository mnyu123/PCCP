# 4번 해설
from collections import deque
import heapq


def add_queue(heap, program, time):
    # 호출 시각이 가장 작은 녀석의 호출 시간이 지금보다 빠르면
    while program and program[0][1] <= time:
        # 대기열 큐에 program[0]을 추가
        heapq.heappush(heap, program.popleft())
    return heap


def solution(program):
    answer = [0] * 11
    # 랭크 , 호출된 시간 , 실행 시간
    # 프로그램을 대기열에 집어넣겠음

    # 프로그램을 호출 시각 기준으로 정렬을 먼저함
    def order(x):
        # x : program의 원소
        # x[1] : 호출 시각
        return x[1]

    # program = deque(sorted(program, key=lambda x: x[1]))
    program = deque(sorted(program, key=order))
    # 예시를 기준으로 정렬된걸 보면
    # [2, 0, 10], [1, 5, 5], [3, 5, 3], [3, 12, 2]
    heap = []   # 대기열

    while program or heap:
        if heap:
            # 대기열에 뭔가 존재해 ,
            # 거기서 가장 앞에있는 녀석 ,
            # 우선순위가 높은 녀석을 실행시키고 ,
            # 점수를 얻고 , 시간을 더해줌

            execute = heapq.heappop(heap)
            rank, call_time, run_time = execute
            # rank : 프로그램의 랭크
            # call_time : 호출 시각
            # run_time : 실행 시간

            answer[rank] = answer[rank] + (time - call_time)
            # time : 현재 한 프로그램이 끝난 시간
            # 그러면 한 타임 기준으로 첫 프로그램이 실행되서 10초가 지났음
            # 거기서 중간에 5초에 들어온 프로세스가 있음
            # 그러면 time = 10 에서 call time 5초를 빼줘야 대기시간을 알 수있음
            # 그 내용을 answer[rank]에 더해줌

            time += run_time

            # 현재 시간인 time에 실행된 시간인 run_time 시간은 더해줘야함
            # 왜냐면 실행된 시간은 지났기 때문에 더해줘야함
        else:
            time = program[0][1]
        heap = add_queue(heap, program, time)

    # 대기열로 이동할때 현재시간 보다 적은것들만 집어넣겠음
    answer[0] = time
    return answer
