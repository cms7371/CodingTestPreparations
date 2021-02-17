# 1931번 회의실 배정 https://www.acmicpc.net/problem/1931
n = int(input())
meetings = []
for i in range(n):
    meetings.append(tuple(map(int, input().split())))
meetings.sort(key=lambda a: a[1], reverse=True)
meetings.sort(key=lambda a: a[0], reverse=True)
results = [meetings.pop()]
while meetings:
    m = meetings.pop()
    if m[0] >= results[-1][1]:
        results.append(m)
    elif m[1] < results[-1][1]:
        results.pop()
        results.append(m)
print(len(results))
