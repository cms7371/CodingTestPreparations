# https://programmers.co.kr/learn/courses/30/lessons/17685


def solution(words):
    words.sort(reverse=True)
    answer = 0
    temp = 0
    n = len(words)
    for i in range(n):
        if i == n - 1:
            n_temp = 0
        else:
            n_temp = get_similarity(words[i], words[i + 1])
        if temp == len(words[i]):
            answer += temp
        else:
            answer += max(n_temp, temp) + 1
        print(words[i], answer)
        temp = n_temp
    return answer


def get_similarity(s1, s2):
    i = 0
    min_l = min(len(s1), len(s2))
    while i < min_l:
        if s1[i] == s2[i]:
            i += 1
        else:
            break
    return i