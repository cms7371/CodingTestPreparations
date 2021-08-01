# 1068번 트리 https://www.acmicpc.net/problem/1068
n = int(input())
parent = list(map(int, input().split()))
del_node = int(input())
graph = [[] for _ in range(n)]
for i in range(n):
    if parent[i] != -1:
        graph[parent[i]].append(i)
total_leafs = graph.count([])
del_leafs = 0
q = [del_node]
while q:
    now = q.pop(0)
    if len(graph[now]) > 0:
        q.extend(graph[now])
    else:
        del_leafs += 1
if len(graph[parent[del_node]]) == 1:
    total_leafs += 1
print(total_leafs - del_leafs)



