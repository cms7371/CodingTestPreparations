# https://www.acmicpc.net/problem/17398
import sys
input = sys.stdin.readline


def find(a):
    if p[a] != a:
        p[a] = find(p[a])
    return p[a]


def union(a, b):
    if find(a) > find(b):
        weight[find(b)] += weight[find(a)]
        weight[find(a)] = 0
        p[find(a)] = find(b)
    elif find(a) < find(b):
        weight[find(a)] += weight[find(b)]
        weight[find(b)] = 0
        p[find(b)] = find(a)


N, M, Q = map(int, input().split())
connection = [[*map(int, input().split()), True] for _ in range(M)]
disconnection = []
for _ in range(Q):
    d = int(input()) - 1
    connection[d][2] = False
    disconnection.append(d)
p = list(range(N + 1))
weight = [1] * (N + 1)
for s, e, c in connection:
    if c:
        union(s, e)
result = 0
while disconnection:
    s, e, _ = connection[disconnection.pop()]
    if find(s) != find(e):
        result += weight[find(s)] * weight[find(e)]
    union(s, e)
print(result)


