# 2109번 순회강연 https://www.acmicpc.net/problem/2109
from heapq import heappop, heappush
n = int(input())
lectures = []
for _ in range(n):
    p, d = map(int, input().split())
    lectures.append((d, p))
lectures.sort()
q = []
result = 0
due = lectures[-1][0] if lectures else 0
for i in range(due, 0, -1):
    while lectures and lectures[-1][0] >= i:
        heappush(q, -lectures.pop()[1])
    if q:
        result -= heappop(q)
print(result)


