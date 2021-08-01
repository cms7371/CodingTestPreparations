# 1931번 회의실 배정 https://www.acmicpc.net/problem/1931
# 다시 풀어볼만한 문제
# 정렬이 중요한 문제 일찍끝나는 순 + 일찍 시작하는 순으로 정렬해 놓고 정렬하여 맨 첫번째 오는 것을 기준으로 삼아시작(시간 복잡도를 위해 거꾸로했음)
n = int(input())
meetings = []
for _ in range(n):
    start, end = map(int, input().split())
    meetings.append((end, start))
meetings.sort(reverse=True)
current = meetings.pop()[0]
count = 1
while meetings:
    m = meetings.pop()
    if m[1] >= current:
        current = m[0]
        count += 1
print(count)


# 첫 풀이
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
