def solution(myString):
    answer = ""
    for i in myString:
        if i == "a":
            answer += "A"
        elif i == "A":
            answer += i
        else:
            answer += i.lower()
    return answer