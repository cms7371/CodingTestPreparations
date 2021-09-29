# https://programmers.co.kr/learn/courses/30/lessons/68937
from collections import deque


def solution(n, edges):
    tree = [[] for _ in range(n + 1)]
    for s, e in edges:
        tree[s].append(e)
        tree[e].append(s)
    print(tree)

    def explore(node):
        dist = [-1] * (n + 1)
        dist[node] = 0
        q = deque()
        q.append(node)
        while q:
            cur = q.popleft()
            for _next in tree[cur]:
                if dist[_next] == -1:
                    dist[_next] = dist[cur] + 1
                    q.append(_next)
        return dist

    init_dist = explore(1)
    print(init_dist)
    end_point1 = init_dist.index(max(init_dist))
    end_point1_dist = explore(end_point1)
    end_point2 = end_point1_dist.index(max(end_point1_dist))
    end_point2_dist = explore(end_point2)
    end_point1_dist.sort()
    end_point2_dist.sort()
    return max(end_point1_dist[-2], end_point2_dist[-2])