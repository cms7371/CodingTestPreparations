# 책 나눠주기 https://www.acmicpc.net/problem/9576
# 복습 풀이
def find(parent, a):
    if parent[a] != a:
        parent[a] = find(parent, parent[a])
    return parent[a]
def union(parent, a, b):
    parent[b] = find(parent, a)

t = int(input())
output = []
for _ in range(t):
    n, m = map(int, input().split())
    student = [tuple(map(int, input().split())) for _ in range(m)]
    student.sort()
    p = [i for i in range(n + 1)]
    result = 0
    while student:
        s = student.pop()
        num = find(p, s[1])
        if num >= s[0]:
            result += 1
            union(p, num - 1, num)
    output.append(str(result))
print("\n".join(output))
#첫 풀이
def find(parents, a):
    if parents[a] == a:
        return a
    else:
        parents[a] = find(parents, parents[a])
        return parents[a]


def union(parents, a, b):  # 무조건 a에 작은 숫자를 넣어야함
    parents[b] = find(parents, a)



test_num = int(input())
result = []
for t in range(test_num):
    n, m = map(int, input().split())
    data = []
    for _ in range(m):
        data.append(tuple(map(int, input().split())))
    data.sort(reverse=True)
    p = [i for i in range(n + 1)]
    count = 0
    for d in data:
        idx_p = find(p, d[1])
        if idx_p >= d[0]:
            count += 1
            union(p, idx_p - 1, idx_p)
    result.append(count)
for r in result:
    print(r)
