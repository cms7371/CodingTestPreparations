# https://www.acmicpc.net/problem/14659
n = int(input())
data = list(map(int, input().split()))
result = 0
start, end = 0, 1
while True:
    while end != n - 1 and data[start] > data[end]:
        end += 1
    result = max(result, end - start - 1)
    if end == n - 1:
        if data[start] > data[end]:
            result = max(result, end - start)
        break
    else:
        start = end
        end = start + 1
print(result)


# 더블 포인터를 이용하면 시간 제한 넉넉하게 풀 수 있을 것 같음
n = int(input())
data = list(map(int, input().split()))
start = 0
end = 1
result = []
while start != (n - 1):
    if end == n - 1:
        if data[end] < data[start]:
            result.append(end - start)
        else:
            result.append(end - start - 1)
        start = end
    elif data[end] < data[start]:
        end += 1
    else:
        result.append(end - start - 1)
        start = end
        end += 1
print(max(result))
