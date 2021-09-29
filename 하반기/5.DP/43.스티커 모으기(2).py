# https://programmers.co.kr/learn/courses/30/lessons/12971


def solution(sticker):
    n = len(sticker)
    dp = [[0] * 4 for _ in range(n)]  # 1을 뽑지 않고 자신을 뽑았을 때, 뽑지 않았을 때, 1을 뽑고 자신을 뽑, 안뽑
    dp[0] = [0, 0, sticker[0], sticker[0]]
    if n > 1:
        dp[1] = [sticker[1], 0, sticker[0], sticker[0]]
        for i in range(2, len(sticker) - 1):
            pd = dp[i - 1]
            dp[i] = [pd[1] + sticker[i], max(pd[0], pd[1]), pd[3] + sticker[i], max(pd[2], pd[3])]
        dp[-1] = [dp[-2][1] + sticker[-1], max(dp[-2][i] for i in [0, 2, 3])]
    return max(dp[-1])


print(solution([1, 2]))