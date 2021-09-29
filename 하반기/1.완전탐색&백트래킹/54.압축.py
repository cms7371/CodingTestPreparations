# https://programmers.co.kr/learn/courses/30/lessons/17684


def solution(msg):
    zip_dict = {chr(64 + i): i for i in range(1, 27)}
    print(zip_dict)
    zip_idx = 27
    answer = []
    s, e = 0, 1
    while e <= len(msg):
        if msg[s:e] in zip_dict:
            temp = zip_dict[msg[s:e]]
            e += 1
        else:
            zip_dict[msg[s:e]] = zip_idx
            print(f"{msg[s:e]} updated of value {zip_idx}")
            zip_idx += 1
            s = e - 1
            e = s + 1
            answer.append(temp)
    answer.append(temp)
    return answer


print(solution("TOBEORNOTTOBEORTOBEORNOT"))