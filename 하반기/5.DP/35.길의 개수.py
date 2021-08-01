# https://www.acmicpc.net/problem/1533
# 경로의 수를 구하는 문제의 변형 1 초과의 가중치를 가진 그래프에 대해 경로를 구하는 문제
# 컨셉: 1이 넘는 시간이 걸리는 길을 정점을 추가해서 쪼갠다 -> 이때 추가되는 정점은 원래의 한 정점으로부터만 들어오는 간선이 있어야함


def dot(matrix1, matrix2):
    r1, c1 = len(matrix1), len(matrix1[0])
    r2, c2 = len(matrix2), len(matrix2[0])
    matrix3 = [[0] * c2 for _ in range(r1)]
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                matrix3[i][j] += matrix1[i][k] * matrix2[k][j]
            matrix3[i][j] %= 1000003
    return matrix3


N, S, E, T = map(int, input().split())
init_graph = [list(map(int, list(input()))) for _ in range(N)]
# 정점 추가한 그래프 선언 높은 가중치부터 쪼개주기
max_weights = [max(line) for line in init_graph]  # 각 정점의 최대 가중치
DN = N + sum(map(lambda x: max(x - 1, 0), max_weights))  # 각 정점의 가중치 - 1 만큼 정점을 추가해줌
decomposed_graph = [[0] * DN for _ in range(DN)]
for i in range(N):
    for j in range(N):
        decomposed_graph[i][j] = init_graph[i][j]
via = N  # 추가된 노드의 위치를 가르키는 변수
for node, weight in enumerate(max_weights):  # 각 노드의 최대 거리부터 순회
    for dist in range(weight, 1, -1):
        for destination in range(via):
            if decomposed_graph[node][destination] == dist:
                decomposed_graph[node][destination] = 0
                decomposed_graph[node][via] = dist - 1
                decomposed_graph[via][destination] = 1
        via += 1  # 다음 경유 노드로
result_graph = [line[:] for line in decomposed_graph]
stack = []
while T != 1:
    if T % 2 == 0:
        stack.append(True)
        T //= 2
    else:
        stack.append(False)
        T -= 1
while stack:
    if stack.pop():
        result_graph = dot(result_graph, result_graph)
    else:
        result_graph = dot(decomposed_graph, result_graph)
print(result_graph[S - 1][E - 1])