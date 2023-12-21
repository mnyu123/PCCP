from collections import deque
import heapq


def add_queue(heap, program, time):
    # program에 데이터가 존재하고,
    # 호출시각이 가장 작은 녀석!의 호출시간이 지금보다 이르면
    while program and program[0][1] <= time:
        # 대기열에 program[0]을 집어넣겠어!
        # queue.append(program.popleft())
        heapq.heappush(heap, program.popleft())
    return heap


def solution(program):
    answer = [0] * 11
    # 점수, 호출시각, 실행시각
    # 프로그램들을 대기열에 집어넣을꺼야!

    # 프로그램을 호출시각 기준으로 정렬을 할꺼야!
    program = deque(sorted(program, key=lambda x: x[1]))
    heap = []

    while program or heap:
        if heap:
            # 실행이 되었을 때
            execute = heapq.heappop(heap)
            answer[execute[0]] += time - execute[1]

            # 실행이 끝났을 때 시간이 흐른다
            time += execute[2]
        else:
            # 실행이 끝났지만 대기열에 아무것도 없어서 할게 없을 때 시간이 흐릅니다
            time = program[0][1]

        # 흐른 시간을 기준으로 program -> 대기열로 이동
        heap = add_queue(heap, program, time)

    answer[0] = time
    return answer
