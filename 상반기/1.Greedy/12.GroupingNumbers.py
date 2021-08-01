# 1744번 수 묶기 https://www.acmicpc.net/problem/1744
n = int(input())
positives = []
negatives = []
zero_count = 0
for i in range(n):
    k = int(input())
    if k > 0:
        positives.append(k)
    elif k < 0:
        negatives.append(k)
    else:
        zero_count += 1
result = 0
positives.sort()
while len(positives) > 1:
    a = positives.pop()
    if a == 1:
        result += a
        continue
    b = positives.pop()
    if b == 1:
        result += a
        result += b
        continue
    result += a * b
if positives:
    result += positives.pop()
negatives.sort(reverse=True)
while len(negatives) > 1:
    result += negatives.pop() * negatives.pop()
if negatives:
    if not zero_count:
        result += negatives.pop()
print(result)

