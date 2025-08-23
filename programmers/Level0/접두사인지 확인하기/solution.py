def solution(my_string, is_prefix):
    answer = 0
    for i in range(len(my_string)):
        word = []
        w = ""
        for j in range(i):
            w += my_string[j]
            word.append(w)
    print(word)
    if is_prefix in word:
        answer = 1
    else:
        answer = 0
    return answer