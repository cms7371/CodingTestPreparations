# https://programmers.co.kr/learn/courses/30/lessons/42889


def solution(N, stages):
    stages_count = [0] * (N + 2)  # 각 스테이지에 머물러 있는 사람
    for s in stages:
        stages_count[s] += 1
    p_sum = [0] * (N + 2)
    p_sum[-1] = stages_count[-1]  # 각 스테이지에 도달한 사람
    for i in range(N, -1, -1):
        p_sum[i] = p_sum[i + 1] + stages_count[i]
    pre_answer = []
    for i in range(1, N + 1):
        stage_failure = 0 if p_sum[i] == 0 else stages_count[i] / p_sum[i]
        pre_answer.append((stage_failure, i))
    pre_answer.sort(key=lambda x: (-x[0], x[1]))
    answer = list(map(lambda x: x[1], pre_answer))
    return answer