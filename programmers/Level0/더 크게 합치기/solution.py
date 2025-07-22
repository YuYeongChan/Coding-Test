def solution(a, b):
    answer = ''
    a = str(a)
    b = str(b)
    answer1 = int(a + b)
    answer2 = int(b + a)
    if answer1 > answer2:
        answer = answer1
    else:
        answer = answer2
    
    return answer