# https://www.acmicpc.net/problem/10211
# DP 해결법
T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [0] * n
    dp[0] = arr[0]
    for i in range(1, n):
        dp[i] = max(arr[i], arr[i] + dp[i - 1])
    print(max(dp))


# 구간 합 해결법
T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(1, n):
        arr[i] += arr[i - 1]
    result = -(10 ** 9)
    for i in range(n):
        result = max(result, arr[i])
        for j in range(i):
            result = max(result, arr[i] - arr[j])
    print(result)