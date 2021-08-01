# https://www.acmicpc.net/problem/1039
N, K = map(int, input().split())
cur = {str(N)}
k = 0
while cur and k < K:
    k += 1
    _next = set()
    for s in cur:
        for i in range(1, len(s)):
            for j in range(0, i):
                ns = list(s)
                ns[i], ns[j] = ns[j], ns[i]
                ns = "".join(ns)
                if not ns.startswith('0') and ns not in _next:
                    _next.add(ns)
    cur = _next
result = list(cur)
result.sort()
print(result[-1] if cur else -1)
