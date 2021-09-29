# https://www.acmicpc.net/problem/3780
import sys
input = sys.stdin.readline


def find(a):
    if p[a] != a:
        cp = p[a]
        p[a] = find(p[a])
        l[a] += l[cp]
    return p[a]


def union(a, b):
    p[a] = b
    l[a] = abs(a - b) % 1000


T = int(input())
for _ in range(T):
    N = int(input())
    p = list(range(N + 1))
    l = [0] * (N + 1)
    while True:
        cmd = input().split()
        if cmd[0] == 'O':
            break
        if len(cmd) == 2:
            cur = int(cmd[1])
            find(cur)
            print(l[cur])
        else:
            s, e = int(cmd[1]), int(cmd[2])
            union(s, e)