# https://www.acmicpc.net/problem/5719
from heapq import *
import sys
input = sys.stdin.readline
INF = 10 ** 9


def dijkstra(start, end, g):
    global N
    dist = [INF] * N
    via = [[] for _ in range(N)]
    q = [(0, start, start)]
    while q:
        d, cur, prev = heappop(q)
        if d < dist[cur]:
            dist[cur] = d
            via[cur] = [prev]
            for _next in g[cur]:
                dd = g[cur][_next]
                if d + dd < dist[_next]:
                    heappush(q, (d + dd, _next, cur))
        elif d == dist[cur]:
            via[cur].append(prev)
    return dist[end], via


while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    S, E = map(int, input().split())
    graph = [dict() for _ in range(N)]
    for _ in range(M):
        s, e, w = map(int, input().split())
        graph[s][e] = w
    shortest_d, s_path = dijkstra(S, E, graph)
    node, node_to_visit = E, []
    while True:
        for p_node in s_path[node]:
            if p_node != node and node in graph[p_node]:
                del graph[p_node][node]
                node_to_visit.append(p_node)
        if node_to_visit:
            node = node_to_visit.pop()
        else:
            break
    result, _ = dijkstra(S, E, graph)
    print(result if result != INF else -1)