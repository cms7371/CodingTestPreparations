# https://www.acmicpc.net/problem/2287
import sys
input = sys.stdin.readline
K = int(input())
N = int(input())
nums = [int(input()) for _ in range(N)]
for num in nums:
    dp = [{int(i * '1') * K} if i != 0 else None for i in range(9)]
    print(dp)
    for i in range(1, 10):
        if i == 9:
            print('NO')
            break
        for j in range(1, (i + 2) // 2):
            for a in dp[j]:
                for b in dp[i - j]:
                    dp[i].update({a + b, a - b, b - a, a * b})
                    if a != 0:
                        dp[i].add(b // a)
                    if b != 0:
                        dp[i].add(a // b)
        if num in dp[i]:
            print(i)
            break