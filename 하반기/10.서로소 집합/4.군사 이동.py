# https://www.acmicpc.net/problem/11085
# 중량 제한과 비슷한 문제, 서로소 집합을 이용한 새로운 풀이
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


P, W = map(int, input().split())
S, E = map(int, input().split())
path = []
for _ in range(W):
    s, e, w = map(int, input().split())
    path.append((w, s, e))
path.sort()
p = [i for i in range(P + 1)]
while True:
    w, s, e = path.pop()
    union(s, e)
    if find(S) == find(E):
        break
print(w)