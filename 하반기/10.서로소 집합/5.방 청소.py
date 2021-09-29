# https://www.acmicpc.net/problem/9938
import sys
input = sys.stdin.readline


def find(a):
    if p[a] != a:
        p[a] = find(p[a])
    return p[a]


def union(a, b):
    if find(a) > find(b):
        p[find(a)] = find(b)
    elif find(a) < find(b):
        p[find(b)] = find(a)
    else:
        p[find(a)] = 0
        p[find(b)] = 0


N, L = map(int, input().split())
p = [i for i in range(L + 1)]
for _ in range(N):
    l, h = map(int, input().split())
    if find(l) == 0 and find(h) == 0:
        print('SMECE')
    else:
        print('LADICA')
        union(l, h)
