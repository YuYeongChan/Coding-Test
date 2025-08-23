def solution(arr):
    answer = []
    index = []
    for i in range(len(arr)):
        if arr[i] == 2:
            index.append(i)
    if index != []:
        for i in range(min(index), max(index) + 1):
            answer.append(arr[i])
    elif index == []:
        answer.append(-1)
    return answer