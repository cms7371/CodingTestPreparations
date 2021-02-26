# 강의실 배정하기 https://www.acmicpc.net/problem/11000
from heapq import *
n = int(input())
lectures = [tuple(map(int, input().split())) for _ in range(n)]
lectures.sort()
q = [(lectures[0][1], lectures[0][0])]
for i in range(1, n):
    earlier = heappop(q)
    heappush(q, (lectures[i][1], lectures[i][0]))
    if earlier[0] > lectures[i][0]:  # 이전 강의의 끝나는 시간이 다음 강의의 시작 시간보다 작다면
        heappush(q, earlier)
print(len(q))

