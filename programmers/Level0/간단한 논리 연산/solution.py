def solution(x1, x2, x3, x4):
    answer = True
    re1 = True
    re2 = True
    if x1 == False and x2 == False:
        re1 = False
    if x3 == False and x4 == False:
        re2 = False
    if re1 == True and re2 == True:
        answer = True
    else:
        answer = False
    return answer