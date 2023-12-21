# 순열
# 순서 중요 , 중복 허용 X
# nPr = n! / (n-r)!
# nPr = n * (n-1) * (n-2) * ... * (n-r+1)

count = 0  # 경우의 수를 저장할 변수
R = 3  # 선택할 요소의 수

def perm(n, k):
    global count  # 전역 변수 count 사용

    if k == R:  # R개를 모두 선택했을 때 출력

        count += 1  # 경우의 수 증가
        print(arr[:R])  # 선택한 요소만 출력

    else:

        for i in range(k, n):

            arr[i], arr[k] = arr[k], arr[i]

            perm(n, k+1)

            arr[i], arr[k] = arr[k], arr[i]

arr = [1, 2, 3, 4, 5]
perm(5, 0)
print("조합결과 :", count)  # 경우의 수 출력