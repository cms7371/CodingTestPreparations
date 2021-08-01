# https://www.acmicpc.net/problem/2661
# 첫번째 스택을 이용하여


def check(num_list):
    l = len(num_list)
    for i in range(1, l // 2 + 1):
        if num_list[-i:] == num_list[-2 * i:-i]:
            return False
    return True
n = int(input())
result = [1]
while True:
    if result[-1] == 4:
        result.pop()
        result[-1] += 1
    elif check(result):
        if len(result) == n:
            break
        result.append(1)
    else:
        result[-1] += 1
print(*result, sep="")

