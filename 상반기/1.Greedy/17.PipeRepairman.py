# 1449번 수리공 항승 https://www.acmicpc.net/problem/1449
n, l = map(int, input().split())
holes = list(map(int, input().split()))
holes.sort(reverse=True)
current = holes.pop()
result = 1
while holes:
    h = holes.pop()
    if h > current + l - 1:
        current = h
        result += 1
print(result)


