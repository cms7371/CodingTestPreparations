# https://www.acmicpc.net/problem/15748
L, N, F, B = map(int, input().split())
diff = F - B
stops = [tuple(map(int, input().split())) for _ in range(N)]
best_stops = [stops[-1]]
while stops:
    pos, val = stops.pop()
    if val > best_stops[-1][1]:
        best_stops.append((pos, val))
best_stops.reverse()
current = 0
result = 0
for pos, val in best_stops:
    time = (pos - current) * diff
    result += time * val
    current = pos
print(result)



