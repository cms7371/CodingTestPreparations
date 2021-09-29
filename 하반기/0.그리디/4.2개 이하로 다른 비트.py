# https://programmers.co.kr/learn/courses/30/lessons/77885
# LSB와 MSB를 응용
from math import log2


def solution(numbers):
    answer = []
    for num in numbers:
        lowest_0bit = get_lowest_zero_bit(num)
        if lowest_0bit == 1:
            answer.append(num + lowest_0bit)
        else:
            under_0bit = num & (lowest_0bit - 1)
            MSB_under_0bit = 2 ** int(log2(under_0bit))
            answer.append(num + lowest_0bit - MSB_under_0bit)
            print(num, lowest_0bit, under_0bit, MSB_under_0bit)
    return answer


def get_lowest_zero_bit(num):
    not_num = ~num
    return not_num & (-not_num)