def solution(num_list):
    answer = 0
    hap = 0
    gob = 0
    for i in range(len(num_list)):
        if i == 0:
            gob = num_list[i]
            hap += num_list[i]
        else:
            gob *= num_list[i]
            hap += num_list[i]
    if gob < (hap ** 2):
        answer = 1
    elif gob > (hap ** 2):
        answer = 0
    return answer