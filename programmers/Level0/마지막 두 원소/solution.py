def solution(num_list):
    answer = []
    length = len(num_list)
    for i in range(length):
        if i < length - 1:
            answer.append(num_list[i])
        else:
            if num_list[i] > num_list[i - 1]:
                answer.append(num_list[i])
                answer.append(num_list[i] - num_list[i - 1])
            else:
                answer.append(num_list[i])
                answer.append(num_list[i] * 2)
    return answer