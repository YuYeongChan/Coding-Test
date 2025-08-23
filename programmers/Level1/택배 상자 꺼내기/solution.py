def solution(n, w, num):
    answer = 0
    floor = 0
    target_floor = 0
    target_x = 0
    last_box_x = 0
    
    if n % w == 0:
        floor = n // w
    else:
        floor = (n // w) + 1
        
    if num % w == 0:
        target_floor = num // w
    else: 
        target_floor = (num // w) + 1
        
    if target_floor % 2 == 1:
        if num % w == 0:
            target_x = w
        else:
            target_x = num % w
    else:
        if num % w == 0:
            target_x = 1
        else:
            target_x = w - (num % w) + 1
    
    if floor % 2 == 1:
        if n % w == 0:
            last_box_x = w
        else:
            last_box_x = n % w
    else:
        if n % w == 0:
            last_box_x = 1
        else:
            last_box_x = w - (n % w) + 1
    
    if floor % 2 == 0:
        if target_x >= last_box_x:
            answer = floor - target_floor + 1
        else:
            answer = floor - target_floor 
    else:
        if target_x <= last_box_x:
            answer = floor - target_floor + 1
        else:
            answer = floor - target_floor
    return answer