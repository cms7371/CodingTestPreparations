# https://programmers.co.kr/learn/courses/30/lessons/64063
# 2019 카카오 인턴십
# 배열이 아닌 dict로 서로소 집합을 시도해봄
import sys
sys.setrecursionlimit(1000000)


def solution(k, room_number):
    parent = dict()
    answer = []
    for n in room_number:
        p = find(n, parent)
        answer.append(p)
        union(p, p + 1, parent)
    return answer


def find(node, parent):
    if node not in parent:
        parent[node] = node
    elif parent[node] != node:
        parent[node] = find(parent[node], parent)
    return parent[node]


def union(a, b, parent):
    parent[a] = find(b, parent)



print(solution(10, [1,3,4,1,3,1]))