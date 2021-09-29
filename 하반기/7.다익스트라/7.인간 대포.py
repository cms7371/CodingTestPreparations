# https://www.acmicpc.net/problem/10473
from heapq import *
import math
import sys
input = sys.stdin.readline


def get_meter(pos1, pos2):
    dx = abs(pos1[0] - pos2[0])
    dy = abs(pos1[1] - pos2[1])
    return math.sqrt(dx ** 2 + dy ** 2)


pos = []
for _ in range(2):
    pos.append(tuple(map(float, input().split())))
n = int(input())
for _ in range(n):
    pos.append(tuple(map(float, input().split())))
dist = [10e9] * (n + 2)
dist[0] = 0.0
q = [(0.0, 0)]
while q:
    d, cur = heappop(q)
    if cur != 1 and d <= dist[cur]:
        # 뛰어가는 경우
        for i in range(1, 2 + n):
            if i != cur and (get_meter(pos[cur], pos[i]) / 5) + d < dist[i]:
                dist[i] = (get_meter(pos[cur], pos[i]) / 5) + d
                heappush(q, (dist[i], i))
        # 날아가는 경우
        if cur != 0:
            for i in range(1, 2 + n):
                if i != cur:
                    d_in_meter = get_meter(pos[cur], pos[i])
                    extra_meter = abs(50 - d_in_meter)
                    flight_d = extra_meter / 5 + 2 + d
                    if flight_d < dist[i]:
                        dist[i] = flight_d
                        heappush(q, (flight_d, i))
print(dist[1])


