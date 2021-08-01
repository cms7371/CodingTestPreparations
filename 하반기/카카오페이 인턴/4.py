from heapq import heappop, heappush


def solution(ages, wires):
    n = len(ages)
    in_wire = [0] * (n + 1)
    out_wire = [[] for _ in range(n + 1)]
    is_running = [True] * (n + 1)
    answer = []
    pq = []
    for i in range(n):
        heappush(pq, (ages[i], i + 1, True))  # day, target, is_generator 순으로
    for s, e, l in wires:
        out_wire[s].append((e, l))
        in_wire[e] += 1
    while len(answer) < n:
        print(pq)
        day, target, is_generator = heappop(pq)
        if is_generator:
            if is_running[target]:
                is_running[target] = False
                answer.append(target)
                for e, l in out_wire[target]:
                    heappush(pq, (day + l, e, False))
            else:
                continue
        else:
            in_wire[target] -= 1
            if in_wire[target] == 0 and is_running[target]:
                is_running[target] = False
                answer.append(target)
                for e, l in out_wire[target]:
                    heappush(pq, (day + l, e, False))
        print(answer)
    return answer


print(solution([35, 25, 3, 8, 7], [[1, 2, 5], [2, 1, 5], [1, 3, 2], [3, 4, 2], [3, 5, 20], [4, 5, 1]]))
print(solution([8, 13, 5, 8], [[1, 3, 10], [3, 4, 1], [4, 2, 2], [2, 1, 3]]))
