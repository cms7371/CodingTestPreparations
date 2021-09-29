# https://programmers.co.kr/learn/courses/30/lessons/42891


def solution(food_times, k):
    k += 1
    N = len(food_times)
    s_food_times = food_times[:]
    s_food_times.sort()
    prev_food = 0
    i = 0
    while i < N:
        cur_food = s_food_times[i]
        cur_round_time = (N - i) * (cur_food - prev_food)
        if k <= cur_round_time:
            break
        i += 1
        prev_food = cur_food
        k -= cur_round_time
    if i == N:
        return -1
    remaining_food = N - i
    k = (N - i) if k % (N - i) == 0 else k % (N - i)
    count = 0
    for idx, food in enumerate(food_times):
        if food > prev_food:
            count += 1
            if count == k:
                return idx + 1