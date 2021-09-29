# https://programmers.co.kr/learn/courses/30/lessons/12979

def solution(n, stations, w):
    answer = 0
    idx = 0
    width = w * 2 + 1
    for s in stations:
        low, high = s - w, s + w
        if idx < low:
            answer += (low - idx - 1) // width + 1
        idx = high
        print(answer, idx)
    if idx < n:
        answer += (n - idx - 1) // width + 1
    return answer