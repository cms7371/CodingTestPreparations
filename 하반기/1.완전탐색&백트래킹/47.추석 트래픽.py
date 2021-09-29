# https://programmers.co.kr/learn/courses/30/lessons/17676


def solution(lines):
    logs = []
    for line in lines:
        date, time, duration_s = line.split()
        seconds = time_to_seconds(time)
        duration = int(float(duration_s[:-1]) * 1000)
        start_time = seconds - duration + 1
        end_time = seconds
        print(start_time, end_time)
        logs.append((start_time, end_time))
    result = 0
    for cur_log in logs:
        for cur_start in cur_log:
            cur_end = cur_start + 999
            local_result = 0
            for other_start, other_end in logs:
                print(cur_start, cur_end, other_start, other_end)
                if other_start <= cur_end and other_end >= cur_start:
                    local_result += 1
            result = max(result, local_result)
    return result


def time_to_seconds(time):
    h, m, s = map(float, time.split(":"))
    return int((h * 3600 + m * 60 + s) * 1000)
