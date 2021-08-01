# https://programmers.co.kr/learn/courses/30/lessons/67257
# 2020 카카오 인턴십 기출
from itertools import permutations


def solution(expression):
    buf = ""
    operators = set()
    seq = []
    for c in expression:
        if c.isnumeric():
            buf += c
        else:
            operators.add(c)
            seq.append(int(buf))
            buf = ""
            seq.append(c)
    seq.append(int(buf))
    operator_orders = permutations(operators, len(operators))
    result = 0
    for orders in operator_orders:
        temp = seq[:]
        for current in orders:
            temp_temp = []
            if current == "+":
                cal = lambda x, y: x + y
            elif current == "-":
                cal = lambda x, y: x - y
            else:
                cal = lambda x, y: x * y
            i = 0
            while i < len(temp):
                if temp[i] == current:
                    temp_temp[-1] = cal(temp_temp[-1], temp[i + 1])
                    i += 2
                else:
                    temp_temp.append(temp[i])
                    i += 1
            temp = temp_temp
        result = max(result, abs(temp[0]))
    return result



print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))
