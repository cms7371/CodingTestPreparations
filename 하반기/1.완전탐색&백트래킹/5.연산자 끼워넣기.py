# https://www.acmicpc.net/problem/14888
# 참고 상반기 삼성대비 8번임
def cal(val, idx, ops):
    if not(any(ops)):
        global min_result, max_result
        min_result = min(min_result, val)
        max_result = max(max_result, val)
        return
    add, sub, mul, div = ops
    if add > 0:
        cal(val + num_list[idx], idx + 1, (add - 1, sub, mul, div))
    if sub > 0:
        cal(val - num_list[idx], idx + 1, (add, sub - 1, mul, div))
    if mul > 0:
        cal(val * num_list[idx], idx + 1, (add, sub, mul - 1, div))
    if div > 0:
        if val >= 0:
            n_val = val // num_list[idx]
        else:
            n_val = -((-val) // num_list[idx])
        cal(n_val, idx + 1, (add, sub, mul, div - 1))


n = int(input())
num_list = list(map(int, input().split()))
op_list = tuple(map(int, input().split()))
min_result = 10e9
max_result = -10e9
cal(num_list[0], 1, op_list)
print(max_result, min_result, sep="\n")



