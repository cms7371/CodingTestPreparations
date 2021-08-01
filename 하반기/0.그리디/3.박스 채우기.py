# https://www.acmicpc.net/problem/1493
from functools import reduce
length = list(map(int, input().split()))
volume = reduce(lambda acc, cur: acc * cur, length, 1)
n = int(input())
block_stock = []
for _ in range(n):
    block_stock.append(tuple(map(int, input().split())))
block_stock.sort()
result = 0
exp = block_stock[-1][0]
count = 0
while block_stock and (2 ** (exp * 3)) * count != volume:
    c_exp, stock = block_stock.pop()
    count = count * (2 ** ((exp - c_exp) * 3))
    exp = c_exp
    c_goal = reduce(lambda acc, cur: acc * cur, map(lambda x: x // (2 ** exp), length), 1) - count
    if c_goal <= stock:
        result += c_goal
        count += c_goal
    else:
        result += stock
        count += stock
if (2 ** (exp * 3)) * count == volume:
    print(result)
else:
    print(-1)


# 짧은 변을 기준으로 육면체를 3개로 분리함
# 무조건 큰 블럭을 쑤셔넣고 이를 작은 블럭으로 대체한다면?
# 너무 복잡한 접근 방식이 되어버렸음. 육면체를 3개로 분리하는 과정에서 겹치는 부분이 제대로 처리되지 않아서 최적의 해를 구할 수 없음
# 하지만 재미있었음
from math import log
from collections import defaultdict


def get_block(l1, l2, l3, block_dict=None):
    if block_dict is None:
        block_dict = defaultdict(int)
    l_list = [l1, l2, l3]
    print('current wlh', *l_list)
    if 0 in l_list:
        return block_dict
    l_list.sort()
    w, l, h = l_list
    MSB = int(log(w, 2))
    c_num = 2 ** MSB
    print(MSB, c_num)
    wm, lm, hm = w // c_num, l // c_num, h // c_num
    block_dict[MSB] += wm * lm * hm
    wd, ld, hd = wm * c_num, lm * c_num, hm * c_num
    get_block(w - wd, c_num, c_num, block_dict)
    get_block(w, c_num, h - hd, block_dict)
    get_block(w, l - ld, h, block_dict)
    return block_dict



length = map(int, input().split())
n = int(input())
block_stock = []
for _ in range(n):
    block_stock.append(tuple(map(int, input().split())))
block_stock.sort()
optimal_result = get_block(*length)
optimal_result = [(key, optimal_result[key]) for key in optimal_result]
optimal_result.sort()
result = 0
while optimal_result and block_stock:
    print(optimal_result, block_stock)
    o_val, o_count = optimal_result.pop()
    b_val, b_count = block_stock.pop()
    if b_val > o_val:
        optimal_result.append((o_val, o_count))
        continue
    diff = o_val - b_val
    revised_count = o_count * (pow(2, diff) ** 3)
    if revised_count > b_count:
        result += b_count
        optimal_result.append((b_val, revised_count - b_count))
    elif revised_count < b_count:
        result += revised_count
        block_stock.append((b_val, b_count - revised_count))
    else:
        result += b_count
    print(result)
if optimal_result:
    print(-1)
else:
    print(result)