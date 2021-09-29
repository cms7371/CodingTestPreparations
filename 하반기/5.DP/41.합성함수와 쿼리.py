# https://www.acmicpc.net/problem/17435
import sys
input = sys.stdin.readline


def log2(a):
    out = 0
    while a > 1:
        out += 1
        a //= 2
    return out


M = int(input())
arr = [0] + list(map(int, input().split()))
dp = [[0] * (M + 1) for _ in range(19)]
dp[0] = arr
for i in range(1, 19):
    for j in range(1, M + 1):
        dp[i][j] = dp[i - 1][dp[i - 1][j]]
Q = int(input())
for _ in range(Q):
    n, x = map(int, input().split())
    while n != 0:
        lsb = (n & - n)
        x = dp[log2(lsb)][x]
        n -= lsb
    print(x)