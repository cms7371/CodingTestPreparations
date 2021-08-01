# 13904번 과제 https://www.acmicpc.net/problem/13904
from heapq import heappop, heappush
n = int(input())
assignments = []
for _ in range(n):
    assignments.append(tuple(map(int, input().split())))
assignments.sort()
q = []
due = assignments[-1][0]
result = 0
while due != 0:
    while assignments and assignments[-1][0] >= due:
        h = assignments.pop()
        heappush(q, -h[1])
    if q:
        result += - heappop(q)
    due -= 1
print(result)
