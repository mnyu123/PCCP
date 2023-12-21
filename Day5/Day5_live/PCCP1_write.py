# pccp 1번 풀이
# 외톨이 알파벳 문제

# 알파벳이 여러종류가 있는데 한묶음씩 나타내야한다
# ex) aabbbcc -> abc

from collections import defaultdict

before = ""  # 이전문자를 저장할거임


def solution(input_string):
    global before
    dic = defaultdict(int)  # 알파벳 개수를 셀거임
    'a'
    dic['a'] += 1  # a 나온개수 셀거임

    for char in input_string:
        if before == char:  # 이전문자와 같으면
            continue

        dic[char] += 1
        before = char
    print(dic)

    answer = []
    for key, value in dic.items():
        if value > 1:
            answer.append(key)

    if answer:
        answer.sort()

        answer = ''.join(answer)
    else:
        answer = "N"

    return answer


solution("aabbbcca")
