def solution(my_string, is_suffix):
    answer = 0
    words = []
    for i in range(len(my_string) - 1, -1, -1):
        word = ""
        for j in range(i, len(my_string)):
            word += my_string[j]
        words.append(word)
    if is_suffix in words:
        answer = 1
    else:
        answer = 0
    return answer