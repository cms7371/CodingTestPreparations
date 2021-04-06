# 2251번 물통 https://www.acmicpc.net/problem/2251
from collections import deque
from itertools import permutations
cap = list(map(int, input().split()))
dp = [False] * (cap[2] + 1)
dp[cap[2]] = True
q = deque()
cases = list(permutations((0, 1, 2), 2))
visited = {(0, 0, cap[2])}
q.append((0, 0, cap[2]))
while q:
    bottle = q.popleft()
    for i, j in cases:
        if bottle[i] != 0 and bottle[j] < cap[j]:
            n_bottle = [k for k in bottle[:]]
            n_bottle[j] = min(cap[j], bottle[j] + bottle[i])
            n_bottle[i] = bottle[i] - (n_bottle[j] - bottle[j])
            n_bottle = tuple(n_bottle)
            if n_bottle not in visited:
                visited.add(n_bottle)
                q.append(n_bottle)
                if n_bottle[0] == 0:
                    dp[n_bottle[2]] = True
for i in range(cap[2] + 1):
    if dp[i]:
        print(i, end=" ")




