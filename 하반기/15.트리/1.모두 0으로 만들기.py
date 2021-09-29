# https://programmers.co.kr/learn/courses/30/lessons/76503
from heapq import *


def solution(a, edges):
    answer = 0
    n = len(a)
    tree = [set() for _ in range(n)]
    for s, e in edges:
        tree[s].add(e)
        tree[e].add(s)
    q = []
    for i in range(n):
        if len(tree[i]) == 1:
            heappush(q, (abs(a[i]), i))
    while q:
        _, node = heappop(q)
        if tree[node]:
            n_node = tree[node].pop()
        else:
            break
        val = a[node]
        if val:
            answer += abs(val)
            a[node] -= val
            a[n_node] += val
        tree[n_node].remove(node)
        if len(tree[n_node]) == 1:
            heappush(q, (abs(a[n_node]), n_node))
    return -1 if any(a) else answer
