# 13458번 시험 감독 : https://www.acmicpc.net/problem/13458
n = int(input())
peoples = list(map(int, input().split()))
b, c = map(int, input().split())
result = n
for p in peoples:
    rest = p - b
    if rest > 0:
        result += rest // c
        if rest % c != 0:
            result += 1
print(result)