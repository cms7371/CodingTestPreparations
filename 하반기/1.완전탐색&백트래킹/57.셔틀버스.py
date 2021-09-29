# https://programmers.co.kr/learn/courses/30/lessons/17678


def solution(n, t, m, timetable):
    timetable = [time_to_min(time) for time in timetable]
    timetable.sort()
    remaining_bus = n
    remaining_seat = m
    cur_bus_time = 540
    last_time = 0
    for time in timetable:
        to_next = False
        if time <= cur_bus_time:
            remaining_seat -= 1
            if remaining_seat == 0:
                to_next = True
            last_time = time - 1
        else:
            to_next = True
        if to_next:
            if remaining_bus == 1:
                break
            else:
                remaining_bus -= 1
                remaining_seat = m
                cur_bus_time += t
        print(min_to_time(time), remaining_bus, remaining_seat)
    # print(min_to_time(last_time), remaining_bus, remaining_seat)
    if remaining_seat:
        return min_to_time(540 + t * (n - 1))
    else:
        return min_to_time(last_time)


def time_to_min(time):
    hh, mm = map(int, time.split(":"))
    return hh * 60 + mm


def min_to_time(minute):
    return f"{minute // 60:0>2}:{minute % 60:0>2}"