# 카드 합체 놀이 https://www.acmicpc.net/problem/15903
from heapq import heappop, heappush

N, M = map(int, input().split())
cards = list(map(int, input().split()))
q = []
for card in cards:
    heappush(q, card)
while M > 0:
    a = heappop(q)
    b = heappop(q) + a
    a = b
    heappush(q, a)
    heappush(q, b)
    M -= 1
print(sum(q))


