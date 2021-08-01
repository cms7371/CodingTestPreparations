# 1707번 이분 그래프 https://www.acmicpc.net/problem/1707
t = int(input())
test_cases = []
for _ in range(t):
    v, e = map(int, input().split())
    graph = dict()
    for _ in range(e):
        a, b = map(int, input().split())
        if a in graph:
            graph[a].add(b)
        else:
            graph[a] = {b}
        if b in graph:
            graph[b].add(a)
        else:
            graph[b] = {a}
    test_cases.append((v, graph))
output = []
for case in test_cases:
    v, graph = case
    visited = [0] * (v + 1)
    stop = False
    result = "YES"
    for node in graph:
        if not visited[node]:
            visited[node] = True
            stack = [(node, 1)]
            while stack:
                current_node, color = stack.pop()
                for next_node in graph[current_node]:
                    if visited[next_node] == color:
                        stop = True
                        break
                    elif visited[next_node] == 0:
                        next_color = 1 if color == 2 else 2
                        visited[next_node] = next_color
                        stack.append((next_node, next_color))
        if stop:
            result = "NO"
            break
    output.append(result)
print("\n".join(output))
