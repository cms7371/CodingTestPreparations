# https://www.acmicpc.net/problem/1865
# 모든 점에서 시작했다는 의미로 0으로 잡고 가중치가 더 작아지는 경우에만 전파해버려도 됨
import sys
input = sys.stdin.readline
INF = 10 ** 9
T = int(input())
for _ in range(T):
    N, M, W = map(int, input().split())
    path = [[] for _ in range(N + 1)]
    for _ in range(M):
        s, e, w = map(int, input().split())
        path[s].append((e, w))
        path[e].append((s, w))
    for _ in range(W):
        s, e, w = map(int, input().split())
        path[s].append((e, -w))
    visited = [False] * (N + 1)
    for start in range(1, N + 1):
        isCycle = False
        if not visited[start]:
            visited[start] = True
            dist = [INF] * (N + 1)
            dist[start] = 0
            for i in range(N + 1):
                for cur in range(1, N + 1):
                    if dist[cur] != INF:
                        for _next, d in path[cur]:
                            if dist[cur] + d < dist[_next]:
                                dist[_next] = dist[cur] + d
                                visited[_next] = True
                                if i == N:
                                    isCycle = True
                                    break
        if isCycle:
            break
    print("YES" if isCycle else "NO")