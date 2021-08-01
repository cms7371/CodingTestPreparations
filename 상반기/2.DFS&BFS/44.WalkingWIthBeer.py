# 9205번 맥주 마시면서 걸어가기

t = int(input())
cases = []
for _ in range(t):
    n = int(input())
    case = []
    for _ in range(n + 2):
        case.append(tuple(map(int, input().split())))
    cases.append(case)
output = []
for p in cases:
    n = len(p)
    graph = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and abs(p[i][0] - p[j][0]) + abs(p[i][1] - p[j][1]) <= 1000:
                graph[i][j] = True
    for i in range(n):
        for j in range(n):
            if graph[i][j]:
                for k in range(n):
                    if graph[j][k] and i != k:
                        graph[i][k] = True
                        graph[k][i] = True
    output.append("happy" if graph[0][-1] else "sad")
print("\n".join(output))


