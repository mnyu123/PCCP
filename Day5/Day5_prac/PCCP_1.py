def solution(input_string):
    lst = list(input_string)  # 문자열을 리스트로 변환

    solo = []  # 외톨이 문자를 담을 리스트
    seen = []  # 이미 본 문자를 담을 리스트

    for i in range(len(lst)):  # 문자열의 각 문자에 대해
        if lst[i] not in seen:  # 만약 이 문자를 처음 봤다면
            seen.append(lst[i])  # 본 문자 리스트에 추가
            print("지금까지 본 문자들:", seen)
        elif i > 0 and lst[i] != lst[i-1] and lst[i] not in solo:
            # 만약 이 문자가 첫 문자가 아니고, 이전 문자와 다르고, 아직 외톨이 리스트에 없다면
            print("추가할 외톨이 문자:", lst[i])
            print("외톨이 문자의 이전 문자:", lst[i-1])
            print("외톨이 문자의 이전 문자가 외톨이 리스트에 있는지:", lst[i-1] in solo)
            print("외톨이 문자의 이전 문자가 본 문자 리스트에 있는지:", lst[i-1] in seen)
            print("외톨이 문자의 이전 문자와 외톨이 문자가 다른지:", lst[i-1] != lst[i])
            solo.append(lst[i])  # 외톨이 리스트에 추가

    solo.sort()  # 외톨이 리스트를 알파벳 순서로 정렬

    if not solo:  # 만약 외톨이 리스트가 비어있다면
        return "N"  # "N"을 반환

    return ''.join(solo)  # 외톨이 리스트를 문자열로 변환하여 반환


input_string = "zzxxbbz"  # 테스트 문자열
print(solution(input_string))  # 함수 실행 및 결과 출력
