# 11501번 주식 https://www.acmicpc.net/problem/11501
# 복습 풀이
t = int(input())
output = []
for _ in range(t):
    n = int(input())
    future = list(map(int, input().split()))
    pocket = []
    current = 0
    result = 0
    for i in range(n-1, -1, -1):
        if future[i] > current:
            result += current * len(pocket) - sum(pocket)
            pocket = []
            current = future[i]
        else:
            pocket.append(future[i])
    result += current * len(pocket) - sum(pocket)
    output.append(str(result))
print("\n".join(output))
# 내 풀이
t = int(input())
cases = []
for _ in range(t):
    n = int(input())
    cases.append(list(map(int, input().split())))
outputs = []
for case in cases:
    pocket = []
    max_stock = 0
    result = 0
    for i in range(len(case) - 1, -1, -1):
        if case[i] > max_stock:
            while pocket:
                p = pocket.pop()
                if p < max_stock:
                    result += max_stock - p
            max_stock = case[i]
        else:
            pocket.append(case[i])
    while pocket:
        p = pocket.pop()
        if p < max_stock:
            result += max_stock - p
    outputs.append(result)
for o in outputs:
    print(o)

