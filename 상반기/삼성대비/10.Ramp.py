# 14890번 경사로 https://www.acmicpc.net/problem/14890
def travel(line):
    global n, l
    is_ramp = [False] * n
    for i in range(n - 1):
        stop = False
        if line[i] == line[i + 1]:
            continue
        elif line[i] - line[i + 1] == 1:
            if i + l < n and not any(is_ramp[i + 1:i + l + 1]) and all([line[j] == line[i + 1] for j in range(i + 1, i + l + 1)]):
                is_ramp[i + 1:i + l + 1] = [True] * l
            else:
                stop = True
        elif line[i] - line[i + 1] == -1:
            if i - l + 1 >= 0 and not any(is_ramp[i - l + 1:i + 1]) and all([line[j] == line[i] for j in range(i - l + 1, i + 1)]):
                is_ramp[i - l + 1:i + 1] = [True] * l
            else:
                stop = True
        else:
            stop = True
        if stop:
            return False
    return True


n, l = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
# 가로 먼저 탐색
result = 0
for row in range(n):
    passed = travel(graph[row])
    if passed:
        result += 1
for col in range(n):
    graph_line = [graph[row][col] for row in range(n)]
    passed = travel(graph_line)
    if passed:
        result += 1
print(result)