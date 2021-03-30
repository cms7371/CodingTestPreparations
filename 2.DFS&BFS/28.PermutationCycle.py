# 10451번 순열사이클 https://www.acmicpc.net/problem/10451
def find(parent, a):
    if parent[a] != a:
        parent[a] = find(parent, parent[a])
    return parent[a]


def union(parent, a, b):
    if a < b:
        parent[find(parent, b)] = find(parent, a)
    else:
        parent[find(parent, a)] = find(parent, b)


t = int(input())
test_cases = []
for _ in range(t):
    _ = input()
    test_cases.append(list(map(int, input().split())))
output = []
for permutation in test_cases:
    p = [i for i in range(len(permutation) + 1)]
    for i in range(len(permutation)):
        union(p, i + 1, permutation[i])
    for i in range(len(permutation)):
        find(p, i + 1)
    result = len(set(p)) - 1
    output.append(str(result))
print("\n".join(output))



