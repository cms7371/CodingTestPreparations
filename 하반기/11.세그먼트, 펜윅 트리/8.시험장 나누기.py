# https://programmers.co.kr/learn/courses/30/lessons/81305
import sys
sys.setrecursionlimit(10000)


def solution(k, num, links):
    n = len(links)
    isRoot = [True] * n
    for a, b in links:
        if a != -1:
            isRoot[a] = False
        if b != -1:
            isRoot[b] = False
    for i in range(n):
        if isRoot[i]:
            root = i
            break
    left, right = 0, sum(num)

    def explore(node, val_limit, count_limit):
        child_result = []
        if num[node] > val_limit:
            return False
        if links[node][0] != -1:
            child_result.append(explore(links[node][0], val_limit, count_limit))
        if links[node][1] != -1:
            child_result.append(explore(links[node][1], val_limit, count_limit))
        if len(child_result) == 0:
            return 0, num[node]
        elif False in child_result:
            print("현재 노드", node, '결과 child 실패')
            return False
        elif len(child_result) == 1:
            print("현재 노드", node, '결과 child 1개')
            c_count, c_val = child_result[0]
            if c_val + num[node] <= val_limit:
                return c_count, c_val + num[node]
            elif c_count < count_limit:
                return c_count + 1, num[node]
            else:
                return False
        elif len(child_result) == 2:
            print("현재 노드", node, '결과 child 2개')
            count_sum = sum(map(lambda x: x[0], child_result))
            val_sum = sum(map(lambda x: x[1], child_result))
            child_result.sort(key=lambda x: x[1])
            s_child, b_child = child_result
            if count_sum > count_limit:
                return False
            elif num[node] + val_sum <= val_limit:
                return count_sum, num[node] + val_sum
            elif num[node] + s_child[1] <= val_limit and count_sum < count_limit:
                return count_sum + 1, num[node] + s_child[1]
            elif count_sum < count_limit - 1:
                return count_sum + 2, num[node]
            else:
                return False
        else:
            return False

    while left <= right:
        mid = (left + right) // 2
        result = explore(root, mid, k - 1)
        print('현재값', mid, '결과', result)
        if result:
            right = mid - 1
        else:
            left = mid + 1
    answer = left
    return answer


solution(3, [12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1], [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [8, 5], [2, 10], [3, 0], [6, 1], [11, -1], [7, 4], [-1, -1], [-1, -1]])
solution(1, [6, 9, 7, 5], [[-1, -1], [-1, -1], [-1, 0], [2, 1]])
solution(2, [6, 9, 7, 5], [[-1, -1], [-1, -1], [-1, 0], [2, 1]])
solution(4, [6, 9, 7, 5], [[-1, -1], [-1, -1], [-1, 0], [2, 1]])