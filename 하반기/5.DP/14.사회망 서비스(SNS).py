# https://www.acmicpc.net/problem/2533
import sys


def dfs(node, parent):
    for child in tree[node]:
        if child != parent:
            dfs(child, node)
            dp[node][0] += dp[child][1]
            dp[node][1] += min(dp[child])
    return min(dp[node])


sys.setrecursionlimit(1000000)
input = sys.stdin.readline
n = int(input())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)
dp = [[0, 1] for _ in range(n + 1)]
print(dfs(1, 0) if n > 2 else 1)
# print(*dp, *tree, sep="\n")