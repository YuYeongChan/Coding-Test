def solution(intStrs, k, s, l):
    answer = []
    for i in range(len(intStrs)):
        num = ""
        for j in range(s, s + l, 1):
            num += intStrs[i][j]
        num = int(num)
        if num > k:
            answer.append(num)
        
    return answer