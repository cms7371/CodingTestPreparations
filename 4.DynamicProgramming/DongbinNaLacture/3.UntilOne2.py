# 문제 : 나누어 떨어질 때 5로 나누기, 3으로 나누기, 2로 나누기 안되면 1 빼기 4가지 연산을 이용해
# 주어진 수를 1로 만들기 위한 최소 횟수를 구하여라


def calculate(num):
    result = []
    if num % 5 == 0:
        result.append(num // 5)
    if num % 3 == 0:
        result.append(num // 3)
    if num % 2 == 0:
        result.append(num // 2)
    result.append(num - 1)
    return result


x = int(input())
d = [tuple([x])]
count = -1
trigger = True
while trigger:
    count += 1
    n_comp = []
    for c in d[count]:
        if c == 1:
            trigger = False
            continue
        else:
            n_comp.extend(calculate(c))
    d.append(set(n_comp))


print(count)


# 예시 코드
# 컨셉은 정수 i를 1로 만들기 위한 최소 연산 횟수를 ai라고 할 때
# ai = min(ai-1, ai/2, ai/3, ai/5) + 1 임을 이용하여(이 전 단계의 수에 연산 횟수 + 1)
# 바텀업 방식으로 ax까지 구하는 것
x = int(input())
d = [0] * 300000
for i in range(2, x + 1):
    d[i] = d[i - 1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)
print(d[x])
# 결론 -> 내꺼가 더 빨라~

