# https://www.acmicpc.net/problem/12995
# 바꿔말하면 서브트리의 노트 수가 k이상인 모든 노드를 구하라는 말로 해석할 수 있을 것 같음
# 2차원으로는 해결이 매우 힘듦, 3차원 dp를 생각해야하는데
# dp[i][j][k]라고 하면 i 노드에서 k개의 노드를 선택하는데 j개의 자식(순서대로)는 제외하는 경우 라고 하면
# dp[i][j][k]는 왈랄라 모르겠다
# 이차원 dp로 해결하는 방법을 이용해봅시다
# dp[i][k]는 i 노드에서 k개의 노드를 선택하는 경우의 수


def DFS(node, parent):
    for child in path[node]:
        if child != parent:
            tree[node].append(child)
            DFS(child, node)


def DP(node):
    global K
    dp[node][1] = 1  # 바꿔야 할 수도
    n_node = tree[node]
    for c in range(len(n_node)):
        DP(n_node[c])
        if c == 0:
            for i in range(2, K + 1):
                dp[node][i] += dp[n_node[c]][i - 1]
        else:
            for i in range(1, K):  # 현재 노드(+ 이전까지의 subtree)에서 K - i개를 선택하고 다음 subtree에서 i개를 선택하는 경우
                dp[node][K] += dp[node][K - i] * dp[n_node[c]][i]
            temp = dp[node][:]
            # 그리고 지금까지 탐색한 subtree에 대한 값을 현재 노트의 dp에 업데이트 해줌
            # 현재 노드에서 k개를 고르는 경우의 수는(dp[node][k])
            # 추가되는 노드에서 i개를 고르고 현재 노드에서 k - i를 고르는 경우를 곱한 것으로 업데이트가 되어야함
            for k in range(2, K):
                for i in range(1, k):
                    temp[k] += dp[node][k - i] * dp[n_node[c]][i]
            dp[node] = temp



N, K = map(int, input().split())
path = [[] for _ in range(N + 1)]
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    path[u].append(v)
    path[v].append(u)
dp = [[0] * (K + 1) for _ in range(N + 1)]
DFS(1, 0)
DP(1)
result = 0
for idx in range(N + 1):
    result += dp[idx][K]
result = result % 1000000007
print(result, sep="\n")


