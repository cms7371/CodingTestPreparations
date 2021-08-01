# 1976번 여행 가자 https://www.acmicpc.net/problem/1976
# 서로소 집합을 이용한 풀이와 벨만-포드를 이용한 풀이 2가지가 가능할 것 같음
# 두번째 서로소 집합
def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]
def union(a, b):
    if a < b:
        parent[find(b)] = find(a)
    else:
        parent[find(a)] = find(b)
n = int(input())
m = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
plan = [i - 1 for i in list(map(int, input().split()))]
parent = [i for i in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j]:
            union(i, j)
for i in range(n):
    find(i)
print("YES" if all([find(plan[i]) == find(plan[i + 1]) for i in range(m - 1)]) else "NO")

# 첫 번째 벨만-포드
n = int(input())
m = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    graph[i][i] = 1
plan = [i - 1 for i in list(map(int, input().split()))]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            for k in range(n):
                if graph[j][k]:
                    graph[i][k] = 1
                    graph[k][i] = 1
if all([graph[plan[i]][plan[i + 1]] for i in range(m - 1)]):
    print("YES")
else:
    print("NO")