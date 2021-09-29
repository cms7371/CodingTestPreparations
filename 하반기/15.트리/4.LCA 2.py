# https://www.acmicpc.net/problem/11438
# 희소 테이블을 이용하여 LCA를 구하는 방법을 이용함
from math import log2
import sys


input = sys.stdin.readline
N = int(input())
path = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    s, e = map(int, input().split())
    path[s].append(e)
    path[e].append(s)
depth = [0] * (N + 1)
parent = [[0] * 18 for _ in range(N + 1)]
parent[1][0] = 1
child = [1]
cur_d = 0
while child:
    n_child = []
    for node in child:
        depth[node] = cur_d
        for c_node in path[node]:
            if c_node != parent[node][0]:
                n_child.append(c_node)
                parent[c_node][0] = node
    child = n_child
    cur_d += 1
for p in range(1, 18):
    for i in range(1, N + 1):
        parent[i][p] = parent[parent[i][p - 1]][p - 1]
for _ in range(int(input())):
    a, b = map(int, input().split())
    while a != b:
        if depth[b] > depth[a]:
            a, b = b, a
        elif depth[a] > depth[b]:
            diff = depth[a] - depth[b]
            while diff:
                lsb = diff & (-diff)
                diff -= lsb
                a = parent[a][int(log2(lsb))]
        else:
            j = 0
            while j < 18 and parent[a][j + 1] != parent[b][j + 1]:
                j += 1
            a, b = parent[a][j], parent[b][j]
    print(a)





