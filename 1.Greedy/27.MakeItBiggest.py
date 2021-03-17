# 크게 만들기 https://www.acmicpc.net/problem/2812
# 복습 풀이
n, k = map(int, input().split())
num = list(input())
i = 0
r = 0
while r != k:
    if i >= len(num) - 1:
        i -= 1
        num.pop()
        r += 1
    elif int(num[i]) < int(num[i + 1]):
        num.pop(i)
        i = max(0, i - 1)
        r += 1
    else:
        i += 1
print("".join(num))

# 첫 풀이
n, k = map(int, input().split())
s = list(map(int, list(input())))
result_len = n - k
result = []
for num in s:
    while result and k:
        if result[-1] < num:
            result.pop()
            k -= 1
        else:
            break
    result.append(num)
for i in range(result_len):
    print(result[i], end="")

# 왼쪽부터 작은 숫자를 모두 제거 -> 실패 반례 13925 2개
n, k = map(int, input().split())
s = input()
count = [0] * 10
for i in range(len(count)):
    count[i] = s.count(str(i))
goal = [0] * 10
buffer = 0
for i in range(len(count)):
    if count[i] + buffer < k:
        buffer += count[i]
        goal[i] = count[i]
    else:
        goal[i] = k - buffer
        break
result = ""
for c in s:
    i = int(c)
    if i < len(goal) and goal[i]:
        goal[i] -= 1
    else:
        result += c
print(result)
