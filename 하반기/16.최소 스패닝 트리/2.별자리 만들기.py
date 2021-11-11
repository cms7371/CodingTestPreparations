# https://www.acmicpc.net/problem/4386



def get_dist(p1, p2):
    x_square = abs(p1[0] - p2[0]) ** 2
    y_square = abs(p1[1] - p2[1]) ** 2
    return (x_square + y_square) ** 0.5


def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    parent[find(b)] = find(a)



N = int(input())
positions = []
for _ in range(N):
    positions.append(tuple(map(float, input().split())))
edges = []
for i in range(N):
    for j in range(i + 1, N):
        edges.append((get_dist(positions[i], positions[j]), i, j))
edges.sort()
parent = [i for i in range(N)]
answer = 0
for d, i, j in edges:
    if find(i) != find(j):
        union(i, j)
        answer += d
print("{0:.2f}".format(answer))