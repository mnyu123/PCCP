# 달팽이 모양으로 숫자 출력(쥰내 어려움 이걸 니네들은 어케 푸니?)

# 위로가면 i-1 , j
# 내려가면 i+1 , j
# 왼쪽으로 가면 i , j-1
# 오른쪽으로 가면 i , j+1

# 규칙성
# i[0,0,1,-1]    이렇게 봄 [0
# j[-1,1,0,0]              -1]
# 이걸로 4방향을 알수있음.

i, j = 3, 4

fromx = [0, 0, 1, -1]
fromy = [1, -1, 0, 0]

for d in range(4):
    nextx = i + fromx[d]
    nexty = j + fromy[d]

    print(nextx, nexty)