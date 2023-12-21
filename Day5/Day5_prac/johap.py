# 조합
# 스택으로 구현
# 5개중 3개를 뽑는 경우의 수 , 경우를 전부 print

arr = ['a', 'b', 'c', 'd', 'e']  # 5개의 카드
N = len(arr)  # 그게 들어있는 길이(개수로 봐도 됨)

sel = ['', '', '']  # 3개를 뽑아야함
R = len(sel)  # 뽑아야하는 개수
count = 0  # 경우의 수를 저장할 변수


def comb(idx, s_idx):  # 함수
    global count  # 전역 변수 count 사용

    if s_idx == R:  # select 리스트에 3개가 다 꽉차면 4번째 인덱스에 넣으면 안되니까 array out of index 에러 방지용으로 조건을 두고 
        print("조합 하나하나의 결과 : ", sel)
        count += 1  # 경우의 수 증가
        return

    if idx == N:  # 끝까지 갔는데 뽑을게 없다며는
        return  # 종료

    sel[s_idx] = arr[idx]  # 선택된 인덱스에 해당하는 값을 넣어줌
    comb(idx+1, s_idx+1)
    comb(idx+1, s_idx)


comb(0, 0)
print("조합결과 :", count)  # 경우의 수 출력
