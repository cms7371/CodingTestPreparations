# 크게 만들기 https://www.acmicpc.net/problem/2812
n, k = map(int, input().split())
s = input()
result = []
i = 1
while k != 0:
    current = int(s[i])
    if result:
        last = result[-1]
    else:
        result.append(current)
        i += 1
        continue
    if last < current:
        result.pop()
        k -= 1
        continue
    else:
        result.append(current)
        i += 1
print("".join(result))




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





