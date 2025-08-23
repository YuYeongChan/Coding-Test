def solution(q, r, code):
    answer = ''
    y = []
    for i in range(0, len(code), q):
        x = []
        for j in range(i, min(i + q, len(code))):
            x.append(code[j])
        y.append(x)
    for i in range(len(y)):
        if r < len(y[i]):
            answer += y[i][r]
    return answer