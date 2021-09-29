# https://www.acmicpc.net/problem/3078
from collections import deque
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
students = [input() for _ in range(N)]
name_len = [0] * 22
result = 0
dq = deque()
for s in students:
    result += name_len[len(s)]
    name_len[len(s)] += 1
    dq.append(len(s))
    if len(dq) > K:
        name_len[dq.popleft()] -= 1
print(result)