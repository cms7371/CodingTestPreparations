# 9009번 피보나치 https://www.acmicpc.net/problem/9009
# 두번째 : 케이스마다 테이블을 만드는 방법 -> 이게 더 느려
n = int(input())
cases = []
for _ in range(n):
    cases.append(int(input()))
results = []
for c in cases:
    table = [1, 1]
    while table[-1] < c:
        table.append(table[-1] + table[-2])
    result = []
    for i in range(len(table) - 1, 0, -1):
        if table[i] <= c:
            result.append(table[i])
            c -= table[i]
        if c == 0:
            break
    result.sort()
    results.append(result)
for r in results:
    print(" ".join(map(str, r)))


# 첫번째 : 케이스의 최대값에 대한 테이블을 만들고 그 테이블을 이용하는 방법
n = int(input())
max_val = 0
cases = []
for _ in range(n):
    cases.append(int(input()))
    max_val = max(max_val, cases[-1])
table = [1, 1]
while table[-1] < max_val:
    table.append(table[-1] + table[-2])
results = []
for c in cases:
    result = []
    for i in range(len(table) - 1, 0, -1):
        if table[i] <= c:
            result.append(table[i])
            c -= table[i]
        if c == 0:
            break
    result.sort()
    results.append(result)
for r in results:
    print(" ".join(map(str, r)))







