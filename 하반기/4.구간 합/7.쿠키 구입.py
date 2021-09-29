# https://programmers.co.kr/learn/courses/30/lessons/49995



def solution(cookie):
    n = len(cookie)
    for i in range(1, n):
        cookie[i] += cookie[i - 1]
    answer = 0
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            mid = (i + j) // 2
            left = cookie[mid] - cookie[i - 1] if i > 0 else cookie[mid]
            right = cookie[j] - cookie[mid]
            if left > right:
                for k in range(mid - 1, i - 1, -1):
                    left = cookie[k] - cookie[i - 1] if i > 0 else cookie[k]
                    right = cookie[j] - cookie[k]
                    if left == right:
                        answer = max(answer, left)
                        break
                    elif left < right:
                        break
            elif left < right:
                for k in range(mid + 1, j):
                    left = cookie[k] - cookie[i - 1] if i > 0 else cookie[k]
                    right = cookie[j] - cookie[k]
                    if left == right:
                        answer = max(answer, left)
                        break
                    elif left > right:
                        break
            else:
                answer = max(answer, left)
                break
    return answer

sum()