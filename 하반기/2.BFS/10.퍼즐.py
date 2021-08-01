# https://www.acmicpc.net/problem/1525
offset = [1, -1, 3, -3]
table = [list(map(int, input().split())) for _ in range(3)]
init = "".join(["".join(map(str, line)) for line in table])
answer = "123456780"
cur = [init]
visited = {init}
t = 0
while cur and answer not in visited:
    t += 1
    _next = []
    for s in cur:
        pos = s.find("0")
        for o in [3, -3, 1, -1]:
            if (pos % 3 == 0 and o == -1) or (pos % 3 == 2 and o == 1):
                continue
            if 0 <= pos + o < len(s):
                ns = list(s)
                ns[pos], ns[pos + o] = ns[pos + o], ns[pos]
                ns = "".join(ns)
                if ns not in visited:
                    _next.append(ns)
                    visited.add(ns)
    cur = _next
print(t if answer in visited else -1)
