def solution(my_string, overwrite_string, s):
    answer = ''
    for i in range(0, len(my_string), 1):
        if i < s:
            answer += my_string[i]
        elif i >= s and i < (len(overwrite_string) + s):
            answer += overwrite_string[i - s]
        else:
            answer += my_string[i]
    return answer