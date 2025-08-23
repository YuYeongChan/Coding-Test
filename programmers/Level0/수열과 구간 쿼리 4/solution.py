def solution(arr, queries):
    answer = []
    for i in range(len(queries)):
        s, e, k = queries[i]
        for j in range(s, e + 1):
            if j % k == 0:
                arr[j] = arr[j] + 1
    answer = arr
    return answer