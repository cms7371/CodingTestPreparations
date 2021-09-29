# https://www.acmicpc.net/problem/15459
# 파라매트릭 서치를 이용한 풀이?
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
hay = []
spicy = []
for _ in range(N):
    f, s = map(int, input().split())
    hay.append((f, s))
    spicy.append(s)
spicy.sort()
l, r = 0, N - 1
while l <= r:
    mid = (l + r) // 2
    cur_s = spicy[mid]
    f_sum = 0
    for i in range(N):
        if hay[i][1] <= cur_s:
            f_sum += hay[i][0]
        else:
            f_sum = 0
        if f_sum >= M:
            break
    if f_sum >= M:
        r = mid - 1
    else:
        l = mid + 1
print(spicy[l])

# 서로소 집합을 이용한 풀이
import sys
input = sys.stdin.readline


def find(a):
    if p[a] != a:
        p[a] = find(p[a])
    return p[a]


def union(a, b):
    if a > b:
        hay[find(b)] += hay[find(a)]
        hay[find(a)] = 0
        p[find(a)] = find(b)
    elif a < b:
        hay[find(a)] += hay[find(b)]
        hay[find(b)] = 0
        p[find(b)] = find(a)


N, M = map(int, input().split())
hay = []
spiciness = []
p = list(range(N))
sort_hay = []
for i in range(N):
    f, s = map(int, input().split())
    hay.append(f)
    spiciness.append(s)
    sort_hay.append((s, i))
sort_hay.sort()
for s, pos in sort_hay:
    if pos - 1 >= 0 and spiciness[pos - 1] <= s:
        union(pos, pos - 1)
    if pos + 1 < N and spiciness[pos + 1] <= s:
        union(pos + 1, pos)
    if hay[find(pos)] >= M:
        break
print(s)