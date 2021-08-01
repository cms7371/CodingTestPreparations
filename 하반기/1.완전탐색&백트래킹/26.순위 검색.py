# https://programmers.co.kr/learn/courses/30/lessons/72412
# 2021 KAKAO BLIND RECUITMENT
# TODO: 다른 방식으로 효율적으로 다시 풀어보기






# 무식하게 db 만들어서 풀기 -> 통과는 했으나 매우 비효율적
def solution(info, query):
    db = [[[[[0] * 100001 for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(3)]
    l_dict = {'cpp': [0], 'java': [1], 'python': [2], '-': [0, 1, 2]}
    p_dict = {'backend': [0], 'frontend': [1], '-': [0, 1]}
    c_dict = {'junior': [0], 'senior': [1], '-': [0, 1]}
    f_dict = {'chicken': [0], 'pizza': [1], '-': [0, 1]}
    for string in info:
        s = string.split()
        s[-1] = int(s[-1])
        l, p, c, f = l_dict[s[0]][0], p_dict[s[1]][0], c_dict[s[2]][0], f_dict[s[3]][0]
        db[l][p][c][f][s[-1]] += 1
    for l in range(3):
        for p in range(2):
            for c in range(2):
                for f in range(2):
                    for n in range(99999, -1, -1):
                        db[l][p][c][f][n] += db[l][p][c][f][n + 1]
    answer = []
    for q in query:
        q = q.split()
        q = [s for s in q if s != 'and']
        ll, pl, cl, fl, n = l_dict[q[0]], p_dict[q[1]], c_dict[q[2]], f_dict[q[3]], int(q[-1])
        result = 0
        for l in ll:
            for p in pl:
                for c in cl:
                    for f in fl:
                        result += db[l][p][c][f][n]
        answer.append(result)

    return answer


print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))