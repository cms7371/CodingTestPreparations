from collections import deque


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, v, visited, deque):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            deque.append(i)
    try:
        bfs(graph, deque.popleft(), visited, deque)
    except IndexError:
        return


def bfs_example(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end="")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


# 그래프는 보통 1부터 주어져 있어서 0번째는 사용하지 않음
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

dfs(graph, 1, visited)

visited = [False] * 9

bfs(graph, 1, visited, deque())
