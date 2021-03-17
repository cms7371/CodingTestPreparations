# 1697번 숨바꼭질 https://www.acmicpc.net/problem/1697
n, k = map(int, input().split())
current = {n}
time = 0
visited = {n}
while k not in visited:
    time += 1
    future = set()
    for c in current:
        if c + 1 not in visited and 0 <= c + 1 <= 100000:
            visited.add(c + 1)
            future.add(c + 1)
        if c - 1 not in visited and 0 <= c - 1 <= 100000:
            visited.add(c - 1)
            future.add(c - 1)
        if c * 2 not in visited and 0 <= c * 2 <= 100000:
            visited.add(c * 2)
            future.add(c * 2)
    del current
    current = future
print(time)