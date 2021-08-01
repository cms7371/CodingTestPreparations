# https://programmers.co.kr/learn/courses/30/lessons/72413
# 2021 KAKAO BLIND RECUITMENT
from heapq import heappush, heappop
INF = int(10e12)


def solution(n, s, a, b, fares):
    path = [[] for _ in range(n + 1)]
    for start, end, cost in fares:
        path[start].append((end, cost))
        path[end].append((start, cost))
    dist_s = dijkstra(s, n, path)
    dist_a = dijkstra(a, n, path)
    dist_b = dijkstra(b, n, path)
    answer = INF
    for i in range(1, n + 1):
        answer = min(answer, dist_s[i] + dist_a[i] + dist_b[i])
    return answer


# 방문한 노드 값이 더 작다면 다시 방문해줘야함
def dijkstra(start, n, graph):
    dist = [INF] * (n + 1)
    q = [(start, 0)]
    while q:
        node, c = heappop(q)
        if dist[node] > c:
            dist[node] = c
            for _next, dc in graph[node]:
                heappush(q, (_next, c + dc))
    return dist




print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))