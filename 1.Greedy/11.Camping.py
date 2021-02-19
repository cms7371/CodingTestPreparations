# 4796번 캠핑 : https://www.acmicpc.net/problem/4796
l, p, v = map(int, input().split())
test_cases = []
while l + p + v != 0:
    test_cases.append((l, p, v))
    l, p, v = map(int, input().split())
for i in range(len(test_cases)):
    l, p, v = test_cases[i]
    result = 0
    while v >= p:
        v -= p
        result += l
    if v > l:
        result += l
    else:
        result += v
    print("Case {0}: {1}".format(i + 1, result))
