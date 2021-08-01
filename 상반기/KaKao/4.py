from collections import deque


def solution(n, start, end, roads, traps):
    graph = [[0] * n for _ in range(n)]
    # 노드 번호 1 빼서 생각
    start -= 1
    end -= 1
    traps = [t - 1 for t in traps]
    traps = set(traps)
    for s, e, d in roads:
        if graph[s - 1][e - 1] != 0:
            graph[s - 1][e - 1] = min(graph[s - 1][e - 1], d)
        else:
            graph[s - 1][e - 1] = d
    q = deque()
    visited = [0] * n
    visited[start] = 1
    q.append((start, 0, visited))
    print(graph)
    answer = 10e9
    while q:
        current, dist, visited = q.popleft()
        if current == end:
            answer = min(answer, dist)
        elif current in traps:
            for next_node in range(n):
                if next_node != current and next_node in traps:
                    if visited[next_node] < 2:
                        if graph[current][next_node] and (visited[next_node] + visited[current]) % 2 == 0:
                            n_visited = visited[:]
                            n_visited[next_node] += 1
                            q.append((next_node, dist + graph[current][next_node], n_visited))
                        elif graph[next_node][current] and (visited[next_node] + visited[current]) % 2 == 1:

                            n_visited = visited[:]
                            n_visited[next_node] += 1
                            q.append((next_node, dist + graph[next_node][current], n_visited))
                else:
                    if visited[next_node] < 2:
                        if visited[current] == 1 and graph[next_node][current] != 0:
                            n_visited = visited[:]
                            n_visited[next_node] += 1
                            q.append((next_node, dist + graph[next_node][current], n_visited))
                        elif visited[current] == 2 and graph[current][next_node] != 0:
                            n_visited = visited[:]
                            n_visited[next_node] += 1
                            q.append((next_node, dist + graph[current][next_node], n_visited))
        else:
            for next_node in range(n):
                if next_node in traps:
                    if visited[next_node] == 0 and graph[current][next_node]:
                        n_visited = visited[:]
                        n_visited[next_node] += 1
                        q.append((next_node, dist + graph[current][next_node], n_visited))
                    elif visited[next_node] == 1 and graph[next_node][current]:
                        n_visited = visited[:]
                        n_visited[next_node] += 1
                        q.append((next_node, dist + graph[next_node][current], n_visited))
                else:
                    if visited[next_node] < 2 and graph[current][next_node]:
                        n_visited = visited[:]
                        n_visited[next_node] += 1
                        q.append((next_node, dist + graph[current][next_node], n_visited))
    return answer


print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))
