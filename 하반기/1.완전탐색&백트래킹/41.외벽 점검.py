# https://programmers.co.kr/learn/courses/30/lessons/60062


def solution(n, weak, dist):
    answer = 0
    cur_points = [tuple(weak)]
    dist.reverse()
    for i in range(len(dist)):
        next_points = set()
        for points in cur_points:
            for p in points:
                next_points.add(tuple(filter(lambda a: is_far(p, a, dist[i], n), points)))
        cur_points = next_points
        if tuple() in cur_points:
            break
    if tuple() in cur_points:
        return i + 1
    else:
        return -1


def is_far(s, e, d, n):
    if e >= s:
        return e - s > d
    else:
        return e + n - s > d