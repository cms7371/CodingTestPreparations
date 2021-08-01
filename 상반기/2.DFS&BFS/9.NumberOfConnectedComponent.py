# 11724번 https://www.acmicpc.net/problem/11724
def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]
def union(a, b):
    if a <= b:
        parent[find(b)] = find(a)
    else:
        parent[find(a)] = find(b)
n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
for _ in range(m):
    n1, n2 = map(int, input().split())
    union(n1, n2)
for i in range(n + 1):
    find(i)
result = set(parent)
print(len(result) - 1)


