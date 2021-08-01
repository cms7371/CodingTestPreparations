# https://programmers.co.kr/learn/courses/30/lessons/81304
# 2021 카카오 인턴십
# bit mask를 이용해서 trap들의 모든 상태에 대해 다익스트라
from heapq import heappop, heappush
from collections import defaultdict

INF = int(10e9)


def solution(n, start, end, roads, traps):
    trap_dict = {}
    # bit mask를 위해 트랩 번호를 인덱스에 매칭
    for i in range(len(traps)):
        trap_dict[traps[i]] = pow(2, i)
    path = [[defaultdict(lambda: INF), defaultdict(lambda: INF)] for _ in range(n + 1)]
    for s, e, d in roads:
        path[s][1][e] = min(path[s][1][e], d)  # 나가는 간선은 1 들어가는 간선은 0
        path[e][0][s] = min(path[e][0][s], d)
    dist = [[INF] * pow(2, len(traps)) for _ in range(n + 1)]
    dist[start][0] = 0
    pq = [(0, start, 0, 0)]
    while pq:
        d, now, mask, prev_mask = heappop(pq)
        if d <= dist[now][prev_mask]:
            if now in trap_dict:
                active = bool(mask & trap_dict[now])
            else:
                active = False
            # 현재 노드가 활성화 되어있는지에 따라 나눔
            if active:  # 활성화 되어 있다면
                for _next in path[now][0]:  # 일반 노드와 비활성화 노드에 대해서는 들어오는 간선
                    if _next not in trap_dict or not bool(trap_dict[_next] & mask):
                        if dist[_next][mask] > d + path[now][0][_next]:
                            dist[_next][mask] = d + path[now][0][_next]
                            n_mask = mask | trap_dict[_next] if _next in trap_dict else mask
                            heappush(pq, (dist[_next][mask], _next, n_mask, mask))
                for _next in path[now][1]:  # 활성화 노드에 대해서는 나가는 간선으로
                    if _next in trap_dict and bool(mask & trap_dict[_next]):
                        if dist[_next][mask] > d + path[now][1][_next]:
                            dist[_next][mask] = d + path[now][1][_next]
                            heappush(pq, (dist[_next][mask], _next, mask ^ trap_dict[_next], mask))
            else:  # 활성화 되어 있지 않다면
                for _next in path[now][1]:  # 일반 노드와 비활성화 노드에 대해서 나가는 간선
                    if _next not in trap_dict or not bool(trap_dict[_next] & mask):
                        if dist[_next][mask] > d + path[now][1][_next]:
                            dist[_next][mask] = d + path[now][1][_next]
                            n_mask = mask | trap_dict[_next] if _next in trap_dict else mask
                            heappush(pq, (dist[_next][mask], _next, n_mask, mask))
                for _next in path[now][0]:  # 활성화 노드에 대해서는 들어오는 간선
                    if _next in trap_dict and bool(mask & trap_dict[_next]):
                        if dist[_next][mask] > d + path[now][0][_next]:
                            dist[_next][mask] = d + path[now][0][_next]
                            heappush(pq, (dist[_next][mask], _next, mask ^ trap_dict[_next], mask))
            # # 현재 노드 기준 정방향에 대해서 진행할 때(다음 노드가 활성화되지 않은 trap or 일반 노드일 때)
            # current_path = path[now][0] if active else path[now][1]
            # for _next in current_path:
            #     if _next not in trap_dict:
            #         if dist[_next][mask] > d + current_path[_next]:
            #             dist[_next][mask] = d + current_path[_next]
            #             heappush(pq, (dist[_next][mask], _next, mask, mask))
            #     elif not bool(trap_dict[_next] & mask):  # trap의 bit이 0이라면
            #         if dist[_next][mask] > d + current_path[_next]:
            #             dist[_next][mask] = d + current_path[_next]
            #             n_mask = mask | trap_dict[_next]
            #             heappush(pq, (dist[_next][mask], _next, n_mask, mask))
            # # 현재 노드 기준 반대방향에 대해서 진행할 때(다음 노드가 활성화된 trap)
            # reversed_path = path[now][1] if active else path[now][0]
            # for _next in reversed_path:
            #     if _next in trap_dict and bool(mask & trap_dict[_next]):
            #         if dist[_next][mask] > d + reversed_path[_next]:
            #             dist[_next][mask] = d + reversed_path[_next]
            #             n_mask = mask ^ trap_dict[_next]
            #             heappush(pq, (dist[_next][mask], _next, n_mask, mask))
    return min(dist[end])


print(solution(2, 1, 2, [[1, 2, 3]], []))
print(solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]))
print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))
