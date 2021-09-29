# https://www.acmicpc.net/problem/1351
# set(이진 트리)을 이용


def getSeq(n):
    if n in dp:
        return dp[n]
    global P, Q
    if n // P not in dp:
        getSeq(n // P)
    if n // Q not in dp:
        getSeq(n // Q)
    dp[n] = dp[n // P] + dp[n // Q]
    return dp[n]


N, P, Q = map(int, input().split())
dp = {0: 1}
print(getSeq(N))