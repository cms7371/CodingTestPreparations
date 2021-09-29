# https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    pre_result = []
    uid_dict = {}
    for r in record:
        if r.startswith("Leave"):
            cmd, uid = r.split()
            pre_result.append([uid, "님이 나갔습니다."])
        else:
            cmd, uid, name = r.split()
            if cmd == "Enter":
                pre_result.append([uid, "님이 들어왔습니다."])
                uid_dict[uid] = name
            elif cmd == "Change":
                uid_dict[uid] = name
    answer = []
    for uid, msg in pre_result:
        answer.append(uid_dict[uid] + msg)
    return answer
