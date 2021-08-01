# https://www.acmicpc.net/problem/2637
from collections import deque, defaultdict
import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
path = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)
result = [0] * (N + 1)
for _ in range(M):
    a, b, n = map(int, input().split())
    path[a].append((b, n))
    in_degree[b] += 1
q = deque()
q.append(N)
result[N] = 1
while q:
    now = q.popleft()
    c_num = result[now]
    for n_part, n_num in path[now]:
        in_degree[n_part] -= 1
        result[n_part] += c_num * n_num
        if in_degree[n_part] == 0 and path[n_part]:
            q.append(n_part)
for i in range(1, N):
    if not path[i]:
        print(i, result[i])



# 큐를 이용해하는 BFS는 메모리 폭파
from collections import deque, defaultdict
import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
path = [[] for _ in range(N + 1)]
result = defaultdict(int)
for _ in range(M):
    a, b, n = map(int, input().split())
    path[a].append((b, n))
q = deque()
q.append((N, 1))
while q:
    now, num = q.popleft()
    for n_part, n_num in path[now]:
        if not path[n_part]:
            result[n_part] += num * n_num
        else:
            q.append((n_part, num * n_num))
keys = sorted(result.keys())
for k in keys:
    print(k, result[k])



