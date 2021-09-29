# https://www.acmicpc.net/problem/2250
# 중위 순회를 이용해서 구하기
def DFS(node, h):
    if len(level) <= h:
        level.append([-1, -1])
    l_child, r_child = tree[node]
    if l_child != -1:
        DFS(l_child, h + 1)
    global g_idx
    if level[h][0] == -1:
        level[h][0] = g_idx
    level[h][1] = g_idx
    g_idx += 1
    if r_child != -1:
        DFS(r_child, h + 1)


N = int(input())
tree = [None] * (N + 1)
isRoot = [True] * (N + 1)
for _ in range(N):
    p, c1, c2 = map(int, input().split())
    tree[p] = (c1, c2)
    isRoot[max(c1, 0)], isRoot[max(c2, 0)] = False, False
root = isRoot.index(True, 1)
g_idx = 0
level = []
DFS(root, 0)
result = (0, 0)
for i, w in enumerate(level):
    val = w[1] - w[0] + 1
    if val > result[1]:
        result = (i + 1, val)
print(*result)
# 트리를 일차원으로 만든 후 각 레벨의 왼쪽과 오른쪽을 조회
def DFS(node, h):
    if len(level) <= h:
        level.append([node])
    else:
        level[h].append(node)
    l_child, r_child = tree[node]
    l = DFS(l_child, h + 1) if l_child != -1 else []
    r = DFS(r_child, h + 1) if r_child != -1 else []
    return l + [node] + r


N = int(input())
tree = [None] * (N + 1)
isRoot = [True] * (N + 1)
for _ in range(N):
    p, c1, c2 = map(int, input().split())
    tree[p] = (c1, c2)
    isRoot[max(c1, 0)], isRoot[max(c2, 0)] = False, False
root = isRoot.index(True, 1)
print(tree, isRoot)
level = []
flat_tree = DFS(root, 0)
print(flat_tree)
print(*level, sep='\n')

result = (0, 0)  # 레벨, 너비 순
for i in range(len(level)):
    low, high = level[i][0], level[i][-1]
    cur = flat_tree.index(high) - flat_tree.index(low) + 1
    if cur > result[1]:
        result = (i + 1, cur)
print(*result)