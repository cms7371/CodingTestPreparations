# https://www.acmicpc.net/problem/4195
import sys
input = sys.stdin.readline


def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    if find(a) < find(b):
        size[find(a)] += size[find(b)]
        size[find(b)] = 0
        parent[find(b)] = find(a)
    elif find(b) < find(a):
        size[find(b)] += size[find(a)]
        size[find(a)] = 0
        parent[find(a)] = find(b)


T = int(input())
for _ in range(T):
    N = int(input())
    pid = {}
    parent = []
    size = []
    for _ in range(N):
        p1, p2 = input().split()
        for p in (p1, p2):
            if p not in pid:
                pid[p] = len(parent)
                parent.append(len(parent))
                size.append(1)
        union(pid[p1], pid[p2])
        print(size[find(pid[p1])])
