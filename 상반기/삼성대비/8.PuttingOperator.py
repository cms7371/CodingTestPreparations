# 14888번 연산자 끼워넣기
def calculate(val, idx, add, sub, mul, div):
    if not any((add, sub, mul, div)):
        global max_result, min_result
        max_result = max(val, max_result)
        min_result = min(val, min_result)
    if add > 0:
        calculate(val + numbers[idx], idx + 1, add - 1, sub, mul, div)
    if sub > 0:
        calculate(val - numbers[idx], idx + 1, add, sub - 1, mul, div)
    if mul > 0:
        calculate(val * numbers[idx], idx + 1, add, sub, mul - 1, div)
    if div > 0:
        if val > 0:
            calculate(val // numbers[idx], idx + 1, add, sub, mul, div - 1)
        else:
            calculate(-((-val) // numbers[idx]), idx + 1, add, sub, mul, div - 1)

n = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))
min_result = 10e9
max_result = -10e9
calculate(numbers[0], 1, *operators)
print(max_result)
print(min_result)
# permutations를 활용해 모든 경우의 수 계산
from itertools import permutations
n = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))
orders = []
for i in range(4):
    orders = orders + operators[i] * [i]
orders = set(permutations(orders, len(orders)))
min_result = 10e9
max_result = -10e9
for order in orders:
    result = numbers[0]
    for i in range(1, n):
        op = order[i - 1]
        if op == 0:
            result += numbers[i]
        elif op == 1:
            result -= numbers[i]
        elif op == 2:
            result *= numbers[i]
        else:
            if result >= 0:
                result = result // numbers[i]
            else:
                result = -((-result) // numbers[i])
    min_result = min(min_result, result)
    max_result = max(max_result, result)
print(max_result)
print(min_result)


