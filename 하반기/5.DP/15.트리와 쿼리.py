# https://www.acmicpc.net/problem/15681
import sys
def dfs(node, parent):
    for child in tree[node]:
        if child != parent:
            dfs(child, node)
            dp[node] += dp[child]


input = sys.stdin.readline
sys.setrecursionlimit(1000000)
n, r, q = map(int, input().split())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)
queries = []
for _ in range(q):
    queries.append(int(input()))
dp = [1] * (n + 1)
dfs(r, 0)
for query in queries:
    print(dp[query])

