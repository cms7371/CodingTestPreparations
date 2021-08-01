# https://www.acmicpc.net/problem/16397
N, T, G = map(int, input().split())
t = 0
cur = {N}
visited = [False] * 100000
visited[N] = True
while t < T and cur and G not in cur:
    t += 1
    _next = set()
    for num in cur:
        if num < 99999 and not visited[num + 1]:
            _next.add(num + 1)
            visited[num + 1] = True
        if 0 < num * 2 <= 99999:
            mul_num = (num * 2) - (10 ** (len(str(num * 2)) - 1))
            if not visited[mul_num]:
                _next.add(mul_num)
                visited[mul_num] = True
    cur = _next
print(t if G in cur else "ANG")
