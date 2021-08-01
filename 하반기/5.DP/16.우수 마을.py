# https://www.acmicpc.net/problem/1949
# 사회망 서비스랑 비슷한 문제인 것 같음
import sys


def dfs(node, parent):
    for child in tree[node]:
        if child != parent:
            dfs(child, node)
            # 자식이 하나라도 우수 마을인 케이스에 대해 고민할 필요가 없는게 모든 자식이 우수 마을이 아닌 것이 최적해가 될 수 없음
            # 최대값을 찾다보면 적어도 한 마을은 자신을 선택한 것이 최적해일 것임
            dp[node][0] += max(dp[child])
            dp[node][1] += dp[child][0]


input = sys.stdin.readline
sys.setrecursionlimit(1000000)
n = int(input())
villagers = [0] + list(map(int, input().split()))
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)
dp = [[0, villagers[i]] for i in range(n + 1)]  # 0은 노드가 우수 마을이 아닐 때, 1이면 우수마을일 때
dfs(1, 0)
print(max(dp[1]))
