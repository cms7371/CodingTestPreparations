# 9466번 텀 프로젝트 https://www.acmicpc.net/problem/9466
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    test_cases.append([0] + list(map(int, input().split())))
output = []
for students in test_cases:
    visited = [0] * len(students)
    visited[0] = -1
    for i in range(1, len(students)):
        if not visited[i]:
            stack = [i]
            while True:
                n = students[stack[-1]]
                if visited[n] == i:
                    s = stack.index(n)
                    for j in stack[s:]:
                        visited[j] = -1
                    break
                elif visited[n]:
                    break
                else:
                    stack.append(n)
                    visited[n] = i
    output.append(str(len(students) - visited.count(-1)))
print("\n".join(output))