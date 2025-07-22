def solution(a, d, included):
    answer = 0
    turn = 0
    for i in range(len(included)):
        turn = a + (d * i)
        if included[i] == True:
            answer += turn

    return answer