# 조합
# 스택으로 구현
# 5개중 3개를 뽑는 경우의 수 , 경우를 전부 print

arr = ['a', 'b', 'c', 'd', 'e']
N = len(arr)

sel = ['','','']
R = len(sel)
count = 0  # 경우의 수를 저장할 변수

def comb(idx, s_idx):
    global count  # 전역 변수 count 사용

    if s_idx == R:
        print("조합 하나하나의 결과 : ",sel)
        count += 1  # 경우의 수 증가
        return

    if idx == N:
        return

    sel[s_idx] = arr[idx]
    comb(idx+1, s_idx+1)
    comb(idx+1, s_idx)

comb(0, 0)
print("조합결과 :", count)  # 경우의 수 출력