# https://www.acmicpc.net/problem/1219
import sys
input = sys.stdin.readline
N, S, E, M = map(int, input().split())
path = [[] for _ in range(N)]
for _ in range(M):
    s, e, c = map(int, input().split())
    path[s].append((e, -c))
profit = list(map(int, input().split()))
N_INF = - 10 ** 9
dist = [N_INF] * N
dist[S] = profit[S]
cycleNode = set()
for i in range(N):
    for cur in range(N):
        if dist[cur] != N_INF:
            c = dist[cur]
            for _next, cc in path[cur]:
                if c + cc + profit[_next] > dist[_next]:
                    dist[_next] = c + cc + profit[_next]
                    if i == N - 1:
                        cycleNode.add(cur)
if dist[E] == N_INF:
    print("gg")
elif cycleNode:
    reachable = False
    while cycleNode and not reachable:
        node = cycleNode.pop()
        visited = [False] * N
        visited[node] = True
        for i in range(N - 1):
            for cur in range(N):
                if visited[cur]:
                    for _next, _ in path[cur]:
                        visited[_next] = True
                        if _next in cycleNode:
                            cycleNode.remove(_next)
            if visited[E]:
                break
        if visited[E]:
            reachable = True
    if reachable:
        print("Gee")
    else:
        print(dist[E])
else:
    print(dist[E])