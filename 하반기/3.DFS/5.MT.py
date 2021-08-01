# https://www.acmicpc.net/problem/10265
# 이번에는 사이클을 기준으로 컴포넌트를 분리하도록 하자. 컴포넌트에 있는 사이클이 그 컴포넌트의 최솟값이고
# 변두리로 붙는 친구들은 최댓값을 늘려주는 것이므로 컴포넌트별로 구분해보자
N, K = map(int, input().split())
relation = [0] + list(map(int, input().split()))
visited = [-1] * (N + 1)
components = []
for i in range(1, N + 1):
    if visited[i] == - 1:
        cur = i
        v, s = set(), []
        while True:
            s.append(cur)
            v.add(cur)
            cur = relation[cur]
            if visited[cur] != -1:
                break
            elif cur in v:
                cycle = []
                while True:
                    cycle.append(s.pop())
                    if cycle[-1] == cur:
                        break
                for c in cycle:
                    visited[c] = len(components)
                components.append([len(cycle), len(cycle)])  # comp의 최소, 최댓값
                break
        while s:
            cur = s.pop()
            belongs = visited[relation[cur]]
            visited[cur] = belongs
            components[belongs][1] += 1
dp = [True] + [False] * K
components.sort(key=lambda x: x[0] - x[1])
for i in range(len(components)):
    low, high = components[i]
    if i > 0:
        for num in range(K, 0, -1):
            if (num - high >= 0 and dp[num - high]) or (num - low >= 0 and dp[num - low]):
                dp[num] = True
    for j in range(low, high + 1):
        if j <= K:
            dp[j] = True
        else:
            break
for i in range(K, -1, -1):
    if dp[i]:
        print(i)
        break

# 실패 -> 원하는대로 노드는 재정의 하였으나 우선순위에 의해 DP가 제대로 적용되지 않아서 최적해를 구할 수 없음
# 스택을 이용한 DFS 접근
# 각 노드에 대해 DFS를 돌려서 사이클을 노드로 묶어버리고 각 노드의 순서에 따라 노드 재정의
N, K = map(int, input().split())
relation = [0] + list(map(int, input().split()))
visited = [-1] * (N + 1)
n_graph = [(10**9, 0)]
for i in range(1, N + 1):
    if visited[i] == - 1:
        cur = i
        v, s = set(), []
        while True:
            s.append(cur)
            v.add(cur)
            cur = relation[cur]
            if visited[cur] != -1:
                break
            elif cur in v:
                cycle = []
                while True:
                    cycle.append(s.pop())
                    if cycle[-1] == cur:
                        break
                print(cycle)
                for c in cycle:
                    visited[c] = len(n_graph)
                n_graph.append((len(cycle), len(n_graph), 0))  # node크기, 현재 id, 선행 노드 id
                break
        while s:
            cur = s.pop()
            _next = relation[cur]
            visited[cur] = len(n_graph)
            n_graph.append((1, len(n_graph), visited[_next]))
print(n_graph)
print(visited)
n_graph.sort(key=lambda x: (-x[0], x[2]))
print(n_graph)
dp = [0]
dp_v = [{0}]
for i in range(1, len(n_graph)):
    val, cur_id, prev = n_graph[i]
    cur_max, cur_v = 0, {0}
    for j in range(0, i):
        if K >= dp[j] + val > cur_max and prev in dp_v[j]:
            cur_max, cur_v = dp[j] + val, dp_v[j].union({cur_id})
    dp.append(cur_max)
    dp_v.append(cur_v)
print(max(dp))









# A를 태우기 위해서는 몇명을 태워야 하는가로 접근
# dp, DFS, 서로소 집합 이용 -> 잘못된 접근 방법
# 서로소 집합을 이용하게 되면 사이클 외부의 노드가 선택적으로 골라질 수 없음
def find(parent, node):
    if parent[node] != node:
        parent[node] = find(parent, parent[node])
    return parent[node]


def union(parent, a, b):
    if b > a:
        parent[find(parent, b)] = find(parent, a)
    else:
        parent[find(parent, a)] = find(parent, b)



N, K = map(int, input().split())
relation = [0] + list(map(int, input().split()))
chain_num = [0] * (N + 1)
p = [i for i in range(N + 1)]
for i in range(1, N + 1):
    visited = set()
    count = 0
    cur = i
    while True:
        visited.add(cur)
        union(p, cur, relation[cur])
        cur = relation[cur]
        count += 1
        if cur in visited:
            break
    chain_num[i] = count
dp = [0] * (N + 1)
dp_v = [set()]
for i in range(1, N + 1):
    cur_max = chain_num[i] if chain_num[i] <= K else 0
    cur_v = {find(p, i)} if chain_num[i] <= K else set()
    for j in range(1, i):
        if K >= dp[j] + chain_num[i] > cur_max and find(p, i) not in dp_v[j]:
            cur_max, cur_v = dp[j] + chain_num[i], dp_v[j].union({find(p, i)})
    dp[i] = cur_max
    dp_v.append(cur_v)
print(chain_num)
print(p)
print(dp)
print(max(dp))