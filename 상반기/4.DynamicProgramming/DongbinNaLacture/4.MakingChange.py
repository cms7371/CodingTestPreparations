# 문제 : 주어진 화폐 단위들을 이용하여 M원을 거슬러 줄 때 필요한 최소 화폐 개수를 구하여라(불가능하면 -1 출력)
n, m = map(int, input().split())
currencies = []
for i in range(n):
    currencies.append(int(input()))
d = [-1] * 10001
for c in currencies:
    d[c] = 1
for i in range(max(currencies), m + 1):
    result = []
    for c in currencies:
        if d[i - c] != -1:
            result.append(d[i - c] + 1)
    if result:
        d[i] = min(result)
print(d[m])

