# https://programmers.co.kr/learn/courses/30/lessons/72414
# 2021 KAKAO BLIND RECUITMENT
# dp와 누적합을 응용한 방식으로 구간 동안 시청한 시간이 가장 많은 구간을 구함
# 4.구간 합/2.개똥벌래 문제와 비슷한 풀이


def time_to_seconds(string):
    h, m, s = map(int, string.split(':'))
    s += 3600 * h + 60 * m
    return s


def solution(play_time, adv_time, logs):
    play_seconds = time_to_seconds(play_time)
    adv_seconds = time_to_seconds(adv_time)
    dp = [0] * (play_seconds + 1)
    for log in logs:
        start, end = log.split('-')
        start, end = time_to_seconds(start), time_to_seconds(end)
        dp[start] += 1
        dp[end] -= 1
    for i in range(1, len(dp)):
        dp[i] += dp[i - 1]
    for i in range(1, len(dp)):
        dp[i] += dp[i - 1]
    # i = 0에서 예외처리 -> 0일 때 값으로 초기화해줌
    answer = 0
    max_time = dp[adv_seconds]
    for i in range(1, len(dp) - adv_seconds):
        # i ~ i + adv까지 누적 시청 시간은 i ~ i + adv - 1까지 더한 값이므로
        if dp[i + adv_seconds - 1] - dp[i - 1] > max_time:
            answer = i
            max_time = dp[i + adv_seconds - 1] - dp[i - 1]
    h, m, s = answer // 3600, (answer % 3600) // 60, answer % 60
    answer = "{0:>02d}:{1:>02d}:{2:>02d}".format(h, m, s)
    return answer


# i ~ i + adv 까지의 합은 i + adv 에서 i