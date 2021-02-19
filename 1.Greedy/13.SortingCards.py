# 1715번 카드 정렬하기 https://www.acmicpc.net/problem/1715
import heapq

n = int(input())
q = []
for i in range(n):
    heapq.heappush(q, int(input()))
result = 0
while len(q) > 1:
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    result += a + b
    heapq.heappush(q, a + b)
print(result)



