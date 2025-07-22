def solution(my_string, k):
    answer = ''
    for i in range(k):
        for j in range(len(my_string)):
            answer += my_string[j]
    return answer