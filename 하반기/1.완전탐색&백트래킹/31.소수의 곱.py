# https://www.acmicpc.net/problem/2014
# 개선 버전 -> 곱하는 과정에서 해당하는 소수로 나눠지는 수를 만나면 멈춤
# -> 겹치는 수 없이 작은 수부터 모두 구할 수 있음
from heapq import *
K, N = map(int, input().split())
prime = list(map(int, input().split()))
pq = prime[:]
for i in range(N):
    num = heappop(pq)
    for p in prime:
        _next = num * p
        heappush(pq, _next)
        if num % p == 0:
            break
    print(pq)
print(num)



from heapq import heappop, heappush, heapify
K, N = map(int, input().split())
prime = list(map(int, input().split()))
prime.sort()
limit = 2 ** 31
pq = prime[:]
heapify(pq)
visited = set(prime)
max_num = 0
trigger = False
for i in range(N):
    num = heappop(pq)
    for p in prime:
        _next = num * p
        if _next > limit:
            break
        if _next not in visited:
            heappush(pq, _next)
            visited.add(_next)
            if not trigger:
                max_num = max(max_num, _next)
                if len(pq) > N * 2:
                    limit = max_num
                    trigger = True
print(num)

