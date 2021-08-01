# https://www.acmicpc.net/problem/16437
# 스택을 이용하여 처음 들어갔을 때는 방문하여 자식노드 스택에, 다시 방문하면 꺼내며 부모에 값 반환
from collections import defaultdict
n = int(input())
child_dict = defaultdict(list)  # 자식 노드로 가는 경로를 표시
values = [0] * (n + 1)  # 양이나 늑대의 수를 저장하는 배열, 늑대의 수는 마이너스로
for i in range(2, n + 1):
    t, a, p = input().split()
    a, p = int(a), int(p)
    values[i] = a if t == "S" else -a
    child_dict[p].append(i)
visited = [False] * (n + 1)
stack = [(1, 0)]
while stack:
    current, parent = stack.pop()
    if not visited[current]:  # 처음으로 방문하는 노드라면 다시 넣고 자식 노드를 추가해줌
        stack.append((current, parent))
        visited[current] = True
        for child in child_dict[current]:  # 다시 방문하면 부모 노드에 자신의 현재값 반영
            stack.append((child, current))
    else:
        values[parent] += values[current] if values[current] > 0 else 0
print(values[1])





# 재귀를 이용해 DFS를 하여 풀기 끝까지 탐색한 후 되돌아오며 윗단 노드에 값을 반환하여 구하기 -> 시간초과 메모리초과
from collections import defaultdict
import sys


def DFS(node):
    if child_dict[node]:
        for path in child_dict[node]:
            values[node] += DFS(path)
    values[node] = 0 if values[node] < 0 else values[node]
    return values[node]


sys.setrecursionlimit(1000000)
n = int(input())
child_dict = defaultdict(list)  # 자식 노드로 가는 경로를 표시
values = [0] * (n + 1)  # 양이나 늑대의 수를 저장하는 배열, 늑대의 수는 마이너스로
for i in range(2, n + 1):
    t, a, p = input().split()
    a, p = int(a), int(p)
    values[i] = a if t == "S" else -a
    child_dict[p].append(i)
print(DFS(1))
