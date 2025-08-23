def solution(my_string, m, c):
    answer = ''
    y = []
    for i in range(0, len(my_string), m):
        x = []
        for j in range(i, i + m):
            x.append(my_string[j])
        y.append(x)
    for i in range(len(y)):
        answer += y[i][c - 1]
    return answer