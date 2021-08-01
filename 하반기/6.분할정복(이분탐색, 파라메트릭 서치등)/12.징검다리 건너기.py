# https://programmers.co.kr/learn/courses/30/lessons/64062
# 2019 카카오 인턴십


def solution(stones, k):
    n = len(stones)
    nums = sorted(list(set(stones)))
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        current = nums[mid]
        i = -1
        while True:
            di = k
            if i + di >= n:
                i += di
                break
            while stones[i + di] < current and di > 0:
                di -= 1
            if di == 0:
                break
            i += di
        if i >= n:
            left = mid + 1
        else:
            right = mid - 1
    answer = nums[right] if right != -1 else 0
    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))