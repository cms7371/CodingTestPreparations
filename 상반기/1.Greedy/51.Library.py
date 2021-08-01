# 1461번 도서관 https://www.acmicpc.net/problem/1461
# 최적화한 둘째 풀이
_, m = map(int, input().split())
nums = map(int, input().split())
p = []
n = []
for a in nums:
    if a > 0:
        p.append(a)
    else:
        n.append(-a)
p.sort()
n.sort()
result = 2 * (sum([p[i] for i in range(len(p) - 1, -1, -m)]) + sum([n[i] for i in range(len(n) - 1, -1, -m)]))
if not n or (p and p[-1] >= n[-1]):
    result -= p[-1]
else:
    result -= n[-1]
print(result)
# 생각나는대로 첫 풀이 100ms
n, m = map(int, input().split())
nums = map(int, input().split())
positive = []
negative = []
for a in nums:
    if a > 0:
        positive.append(a)
    else:
        negative.append(-a)
positive.sort()
negative.sort()
result = 0
if not negative or (positive and positive[-1] >= negative[-1]):
    result += positive[-1]
    positive = positive[:-m]
else:
    result += negative[-1]
    negative = negative[:-m]
while positive:
    result += 2 * positive[-1]
    positive = positive[:-m]
while negative:
    result += 2 * negative[-1]
    negative = negative[:-m]
print(result)