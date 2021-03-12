# 강의실 배정하기 https://www.acmicpc.net/problem/11000
# pq를 이용하여 구함. 강의를 하나씩 큐에 넣고 (끝나는 시간, 시작 시간)으로 가장 빨리 끝나는 강의를 꺼내서 비교한다.
# 만약 큐에서 나온 강의의 끝나는 시간이 현재 넣는 강의의 시작 시간보다 앞이라면 꺼낸 강의를 버리고 현재의 강의를 넣고,
# 아니라면 꺼낸 강의를 다시 넣어서 강의실이 하나 늘어나는 것처럼 구현해준다
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

