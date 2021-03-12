# 1781번 컵라면 https://www.acmicpc.net/problem/1781
from heapq import heappush, heappop


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
        a = assignments.pop()
        heappush(q, (-a[1]))
    if q:
        result -= heappop(q)
    due -= 1
print(result)
