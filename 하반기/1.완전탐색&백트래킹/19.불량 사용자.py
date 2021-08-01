# https://programmers.co.kr/learn/courses/30/lessons/64064


def solution(user_id, banned_id):
    candidate = []
    for bid in banned_id:
        temp = []
        for uid in user_id:
            if len(bid) == len(uid) and all([bid[i] == '*' or bid[i] == uid[i] for i in range(len(bid))]):
                temp.append(uid)
        candidate.append(temp)
    answer = set()
    DFS(candidate, 0, set(), answer)
    return len(answer)


def DFS(candidate, idx, selected, ans):
        for c in candidate[idx]:
            if c not in selected:
                n_selected = set(selected)
                n_selected.add(c)
                if idx == len(candidate) - 1:
                    n_selected = list(n_selected)
                    n_selected.sort()
                    n_selected = "".join(n_selected)
                    ans.add(n_selected)
                else:
                    DFS(candidate, idx + 1, n_selected, ans)


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))