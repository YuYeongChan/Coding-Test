def solution(my_string, n):
    answer = ''
    lenn = len(my_string)
    for i in range(lenn - n, lenn):
        answer += my_string[i]
        
    return answer