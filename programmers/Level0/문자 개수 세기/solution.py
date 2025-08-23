def solution(my_string):
    answer = []
    for i in range(52):
        answer.append(0)
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    for i in range(len(my_string)):
        if my_string[i] in alpha:
            ind = alpha.index(my_string[i])
            answer[ind] += 1
    return answer