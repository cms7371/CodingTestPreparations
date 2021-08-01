# https://www.acmicpc.net/problem/2104
# 히스토그램이랑 비슷한 문제 같음
# 스택을 이용한 풀이





# 재귀를 이용한 분할 탐색
N = int(input())
arr = list(map(int, input().split()))


def solve(start, end):
    if start == end:
        return arr[start] ** 2
    mid = (start + end) // 2
    result = max(solve(start, mid), solve(mid + 1, end))
    l, r = mid, mid
    c_sum = arr[mid]
    _min = arr[mid]
    while start <= l and r <= end:
        result = max(result, c_sum * _min)
        l_min = min(_min, arr[l - 1]) if l > start else -1
        r_min = min(_min, arr[r + 1]) if r < end else -1
        if l_min >= r_min:
            l -= 1
            _min = l_min
            c_sum += arr[l]
        else:
            r += 1
            _min = r_min
            c_sum += arr[r]
    return result


print(solve(0, N - 1))


# 기존 코드
# result = max(result, c_sum * l_min)
# if start < l and r < end:
#     if arr[l - 1] >= arr[r + 1]:
#         l -= 1
#         c_sum += arr[l]
#         l_min = min(l_min, arr[l])
#     else:
#         r += 1
#         c_sum += arr[r]
#         l_min = min(l_min, arr[r])
# elif r < end:
#     r += 1
#     c_sum += arr[r]
#     l_min = min(l_min, arr[r])
# elif start < l:
#     l -= 1
#     c_sum += arr[l]
#     l_min = min(l_min, arr[l])
# else:
#     break