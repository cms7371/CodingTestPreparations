# 12851번 숨바꼭질 2 https://www.acmicpc.net/problem/12851
s, d = map(int, input().split())
if s == d:
    print(0, 1, sep="\n")
else:
    dp = [False] * 100001
    current_p = [s]
    dp[s] = [0, 1]
    dist = 0
    while not dp[d]:
        dist += 1
        next_p = []
        for p in current_p:
            for np in (p + 1, p - 1, p * 2):
                if 0 <= np <= 100000:
                    if not dp[np]:
                        dp[np] = [dist, dp[p][1]]
                        next_p.append(np)
                    elif dp[np][0] == dist:
                        dp[np][1] += dp[p][1]
        current_p = next_p
    print(dp[d][0], dp[d][1], sep="\n")




