# https://www.acmicpc.net/problem/3108
import sys

input = sys.stdin.readline


def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    if find(b) > find(a):
        parent[find(b)] = find(a)
    else:
        parent[find(a)] = find(b)


def is_intersect(s1, s2):
    s1x1, s1y1, s1x2, s1y2 = s1
    s2x1, s2y1, s2x2, s2y2 = s2
    if ((s1y1 <= s2y1 <= s1y2 or s1y1 <= s2y2 <= s1y2) and s2x1 <= s1x2 and s2x2 >= s1x1 and not (
            s2x1 > s1x1 and s2x2 < s1x2)) or (
            (s1x1 <= s2x1 <= s1x2 or s1x1 <= s2x2 <= s1x2) and s2y1 <= s1y2 and s2y2 >= s1y1 and not (
            s2y1 > s1y1 and s2y2 < s1y2)):
        return True
    return False


N = int(input())
square = [tuple(map(int, input().split())) for _ in range(N)]
parent = [i for i in range(N)]
init_val = 1
for i in range(N):
    x1, y1, x2, y2 = square[i]
    if init_val and ((x1 <= 0 and x2 >= 0 and (y1 == 0 or y2 == 0)) or (y1 <= 0 and y2 >= 0 and (x1 == 0 or x2 == 0))):
        init_val = 0
    for j in range(i + 1, N):
        print(square[i], square[j])
        if find(i) != find(j) and is_intersect(square[i], square[j]):
            print("intersect!")
            union(i, j)
print(parent)
for i in range(N):
    find(i)
print(init_val + len(set(parent)) - 1)
