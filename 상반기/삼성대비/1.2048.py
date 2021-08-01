# 12100번 2048 https://www.acmicpc.net/problem/12100
# 2차 간단하게
from collections import deque


def merge(arr):
    nums = [num for num in arr if num != 0]
    idx = 0
    merged = []
    while idx < len(nums):
        if idx != len(nums) - 1 and nums[idx] == nums[idx + 1]:
            merged.append(nums[idx] * 2)
            idx += 2
        else:
            merged.append(nums[idx])
            idx += 1
    return merged + [0] * (n - len(merged))

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
q = deque()
q.append((graph, 0))
result = max([max(l) for l in graph])
while q:
    now_graph, time = q.popleft()
    if time == 5:
        result = max(result, max([max(i) for i in now_graph]))
    else:
        # 왼쪽으로 밀 때
        left_graph = [line[:] for line in now_graph]
        for i in range(n):
            left_graph[i] = merge(left_graph[i])
        if left_graph != now_graph:
            q.append((left_graph, time + 1))
        # 아래로 밀 때
        down_graph = [line[:] for line in now_graph]
        for j in range(n):
            line = merge([down_graph[i][j] for i in range(n - 1, -1, -1)])
            for i in range(n):
                down_graph[i][j] = line[n - i - 1]
        if down_graph != now_graph:
            q.append((down_graph, time + 1))
        # 오른쪽으로 밀 때
        right_graph = [line[:] for line in now_graph]
        for i in range(n):
            right_graph[i] = merge(right_graph[i][::-1])[::-1]
        if right_graph != now_graph:
            q.append((right_graph, time + 1))
        # 위로 밀 때
        up_graph = [line[:] for line in now_graph]
        for j in range(n):
            line = merge([up_graph[i][j] for i in range(n)])
            for i in range(n):
                up_graph[i][j] = line[i]
        if up_graph != now_graph:
            q.append((up_graph, time + 1))
print(result)


# 폐기: 너무 구현에 심취했음 -> 그래프로 직접 이동 안시키고 라인만 따서 연산 후 다시 집어넣는 방식으로 개선 가능
from collections import deque
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
q = deque()
q.append((graph, 0))
result = 0
while q:
    now_graph, time = q.popleft()
    if time == 5:
        result = max(result, max([max(i) for i in now_graph]))
        print("\n".join(map(str, now_graph)))
        print()
    else:
        # 왼쪽으로 밀 때
        next_graph = [line[:] for line in now_graph]
        for i in range(n):
            for j in range(n):
                if j != n - 1:
                    if next_graph[i][j] == 0:
                        dj = 1
                        while j + dj < n and next_graph[i][j + dj] == 0:
                            dj += 1
                        next_graph[i][j:] = next_graph[i][j + dj:] + [0] * dj
                    elif next_graph[i][j] == next_graph[i][j + 1]:
                        next_graph[i][j] *= 2
                        next_graph[i][j + 1] = 0
        if not now_graph == next_graph:
            q.append((next_graph, time + 1))
        # 아래로 밀 때
        next_graph = [line[:] for line in now_graph]
        for j in range(n):
            for i in range(n - 1, -1, -1):
                if i != 0:
                    if next_graph[i][j] == 0:
                        for k in range(i, 0, -1):
                            next_graph[k][j] = next_graph[k - 1][j]
                        next_graph[0][j] = 0
                    elif next_graph[i][j] == next_graph[i - 1][j]:
                        next_graph[i][j] *= 2
                        next_graph[i - 1][j] = 0
        if not now_graph == next_graph:
            q.append((next_graph, time + 1))
        # 오른쪽으로 밀 때
        next_graph = [line[:] for line in now_graph]
        for i in range(n):
            for j in range(n - 1, -1, -1):
                if j != 0:
                    if next_graph[i][j] == 0:
                        next_graph[i][:j + 1] = [0] + next_graph[i][:j]
                    elif next_graph[i][j] == next_graph[i][j - 1]:
                        next_graph[i][j] *= 2
                        next_graph[i][j - 1] = 0
        if not now_graph == next_graph:
            q.append((next_graph, time + 1))
        # 위로 밀 때
        next_graph = [line[:] for line in now_graph]
        for j in range(n):
            for i in range(n):
                if i != n - 1:
                    if next_graph[i][j] == 0:
                        for k in range(i, n - 1):
                            next_graph[k][j] = next_graph[k + 1][j]
                        next_graph[-1][j] = 0
                    elif next_graph[i][j] == next_graph[i + 1][j]:
                        next_graph[i][j] *= 2
                        next_graph[i + 1][j] = 0
        if not now_graph == next_graph:
            q.append((next_graph, time + 1))
print(result)
