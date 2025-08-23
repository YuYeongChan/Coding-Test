def solution(arr, queries):
    answer = []
    for i in range(len(queries)):
        s, e, k = queries[i]
        number = []
        for j in range(s, e + 1):
            if arr[j] > k:
                number.append(arr[j])
        if number:
            answer.append(min(number))
        else:
            answer.append(-1)
            
    return answer