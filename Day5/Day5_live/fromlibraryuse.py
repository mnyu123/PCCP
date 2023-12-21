from itertools import combinations,permutations # 조합 , 순열 순으로 라이브러리를 불러온다.

print(list(combinations([1,2,3,4,5],3))) # 5개의 원소중 3개를 뽑는 조합을 출력한다.
print()
print(list(permutations([1,2,3,4,5],3))) # 5개의 원소중 3개를 뽑는 순열을 출력한다.