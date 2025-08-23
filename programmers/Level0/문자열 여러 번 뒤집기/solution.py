def solution(my_string, queries):
    answer = ''
    start = 0
    end = 0

    for i in range(len(queries)):
        start = queries[i][0]
        end = queries[i][1]
        newString = ''
        for j in range(len(my_string)):
            if j < start:
                newString += my_string[j]
            elif j >= start and j <= end:
                newString += my_string[end + start - j]
            else:
                newString += my_string[j]
        my_string = newString
    answer = my_string
    return answer