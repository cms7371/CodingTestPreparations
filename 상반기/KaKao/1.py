num_list = ["zero", "one", "two", "three", "four",
            "five", "six", "seven", "eight", "nine"]


def solution(s):
    answer = ""
    idx = 0
    max_idx = len(s) - 1
    while idx <= max_idx:
        if s[idx].isnumeric():
            answer += s[idx]
            idx += 1
        else:
            for i in range(10):
                num_str = num_list[i]
                if idx + len(num_str) <= max_idx + 1 and num_str == s[idx:idx+len(num_str)]:
                    answer += str(i)
                    idx += len(num_str)
                    break
    answer = int(answer)
    return answer


print(solution("2three45sixseven"))