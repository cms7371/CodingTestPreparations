# 통나무 건너뛰기 https://www.acmicpc.net/problem/11497
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    test_cases.append(list(map(int, input().split())))
for case in test_cases:
    case.sort()
    print(max([case[i + 2] - case[i] for i in range(len(case) - 2)]))

