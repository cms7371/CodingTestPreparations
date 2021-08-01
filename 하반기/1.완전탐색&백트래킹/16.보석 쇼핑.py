# https://programmers.co.kr/learn/courses/30/lessons/67258
# 2020 카카오 인턴십
# 투포인터로 두번째 풀이
def solution(gems):
    gems_set = set(gems)
    gems_dict = dict()
    for g in gems_set:
        gems_dict[g] = 0
    count = 0
    left, right = 0, -1
    for g in gems:
        if gems_dict[g] == 0:
            count += 1
        gems_dict[g] += 1
        right += 1
        if count == len(gems_set):
            break
    result = [left + 1, right + 1]
    while right < len(gems):
        print(result)
        if gems_dict[gems[left]] > 1 and count == len(gems_set):
            gems_dict[gems[left]] -= 1
            left += 1
            result = [left + 1, right + 1]
        else:
            gems_dict[gems[left]] -= 1
            if gems_dict[gems[left]] == 0:
                count -= 1
            if right < len(gems) - 1:
                gems_dict[gems[right + 1]] += 1
                if gems_dict[gems[right + 1]] == 1:
                    count += 1
            left += 1
            right += 1
    return result



# 탐색으로 푼 첫번째 풀이
# def solution(gems):
#     gem_set = set(gems)
#     gem_dict = dict()
#     for g in gem_set:
#         gem_dict[g] = -1
#     dict_count = 0
#     min_len = len(gems)
#     result = [1, len(gems)]
#     dict_len = len(gem_set)
#     for i in range(len(gems)):
#         if gem_dict[gems[i]] == -1:
#             dict_count += 1
#         gem_dict[gems[i]] = i
#         if dict_count == dict_len:
#             temp_low, temp_high = min(gem_dict.values()), max(gem_dict.values())
#             if temp_high - temp_low + 1 < min_len:
#                 min_len = temp_high - temp_low + 1
#                 result = [temp_low + 1, temp_high + 1]
#     return result



print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))