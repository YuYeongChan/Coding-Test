def solution(num_list):
    answer = 0
    chat = 0
    hole = 0
    for i in range(len(num_list)):
        if i % 2 == 0:
            hole += num_list[i]
        else:
            chat += num_list[i]
    if hole > chat:
        answer = hole
    else:
        answer = chat
    return answer