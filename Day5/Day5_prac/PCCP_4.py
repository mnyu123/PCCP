# 4번 내가 풀어보기

# 프로그램 정보를 나타내는 2차원 정수 배열 program
def solution(program):
    # 프로그램들을 우선 순위에 따라 정렬
    program.sort(key=lambda x: x[0])

    total_running_time = 0  # 프로그램들의 총 실행 시간
    waiting_times = [0] * 10  # 각 프로그램의 대기 시간

    for rank, waiting_time, running_time in program:
        total_running_time += running_time  # 실행 시간 누적
        waiting_times[rank-1] += waiting_time  # 대기 시간 누적

    # 총 실행 시간과 각 프로그램의 대기 시간을 반환
    return [total_running_time] + waiting_times

# rank 프로그램 우선순위 점수 낮을수록 우선순위가 높다
# waiting_time 호출된 프로그램이 실행할때까지 대기한 시간 기록
# running_time 프로그램이 실행되는데 걸리는 시간

# program 이라는 2차원 배열에 rank , waiting_time , running_time 이라는 3가지 정보가 있다
# 그리고 반환되는 정보는 answer[] 일차원 배열에 첫 인덱스에는 프로그램들이 총 실행된 시간
# 두번째 인덱스 부터는 rank 1부터 10까지의 각 전체 프로그램이 실행되기까지 기다린 시간을 저장해아한다.



def program_info(rank, waiting_time, running_time):
    program = [[2, 0, 10], [1, 5, 5], [3, 5, 3], [3, 12, 2]]
    # 프로그램 정보를 하나의 리스트로 묶어서 추가
    program.append([rank, waiting_time, running_time])
    print(program)
    return program
