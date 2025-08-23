def solution(my_string):
    answer = []
    for i in range(0, len(my_string), 1):
        word = ""
        word += my_string[i: len(my_string)]
        answer.append(word)
    answer.sort()
                        
    return answer