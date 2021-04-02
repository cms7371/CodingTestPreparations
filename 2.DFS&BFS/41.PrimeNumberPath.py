# 1963번 소수 경로
from collections import deque
def isAlterable(a, b):
    sa, ba = str(a), str(b)
    count = 0
    for j in range(4):
        if sa[j] == ba[j]:
            count += 1
    return True if count == 3 else False
table = [i + 2 for i in range(9998)]
i = 0
while table[i] < 5000:
    new_table = table[:i + 1]
    for num in table[i + 1:]:
        if num % table[i] != 0:
            new_table.append(num)
    table = new_table
    i += 1
table = [i for i in table if i > 1000]
t = int(input())
cases = [tuple(map(int, input().split())) for _ in range(t)]
output = []
for start, end in cases:
    visited = [False] * len(table)
    i = table.index(start)
    visited[i] = True
    q = deque()
    q.append((i, 0))
    result = -1
    while q:
        idx, dist = q.popleft()
        if table[idx] == end:
            result = dist
        for i in range(len(table)):
            if not visited[i] and isAlterable(table[idx], table[i]):
                q.append((i, dist + 1))
                visited[i] = True
    output.append("Impossible" if result == -1 else str(result))
print("\n".join(output))



