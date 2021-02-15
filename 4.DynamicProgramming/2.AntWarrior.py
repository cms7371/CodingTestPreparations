n = int(input())
storage = list(map(int, input().split()))
dp = [0] * n
for i in range(n):
    if i == 0:
        dp[0] = storage[0]
    elif i == 1:
        dp[1] = max(storage[0], storage[1])
    else:
        dp[i] = max(storage[i] + dp[i - 2], dp[i - 1])
print(dp[-1])
