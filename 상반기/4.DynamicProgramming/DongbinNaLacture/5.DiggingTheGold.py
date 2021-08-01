t = int(input())
test_cases = []
for i in range(t):
    n, m = map(int, input().split())
    line = list(map(int, input().split()))
    graph = [line[i:i + m] for i in range(0, n * m, m)]
    test_cases.append(graph)
results = []
for graph in test_cases:
    n, m = len(graph), len(graph[0])
    d = [[0] * m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            if i == 0:
                d[j][i] = graph[j][i]
            else:
                local_results = []
                if j > 0:
                    local_results.append(d[j-1][i-1] + graph[j][i])
                local_results.append(d[j][i-1] + graph[j][i])
                if j < n - 1:
                    local_results.append(d[j+1][i-1] + graph[j][i])
                d[j][i] = max(local_results)
    results.append(max([d[i][m - 1] for i in range(n)]))
for r in results:
    print(r)


