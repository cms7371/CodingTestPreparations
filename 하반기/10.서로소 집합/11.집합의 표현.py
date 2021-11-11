# https://www.acmicpc.net/problem/1717
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)


def find(p, a):
    if p[a] != a:
        p[a] = find(p, p[a])
    return p[a]


def union(p, a, b):
    if find(p, a) < find(p, b):
        p[find(p, b)] = find(p, a)
    else:
        p[find(p, a)] = find(p, b)


N, M = map(int, input().split())
parent = list(range(N + 1))
for _ in range(M):
    cmd, n1, n2 = map(int, input().split())
    if cmd == 0:
        union(parent, n1, n2)
    else:
        if find(parent, n1) == find(parent, n2):
            print("YES")
        else:
            print("NO")
