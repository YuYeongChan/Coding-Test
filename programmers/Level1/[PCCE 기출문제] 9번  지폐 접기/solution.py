def solution(wallet, bill):
    answer = 0
    bill_long_part = 0
    bill_short_part = 0
    wallet_long_part = 0
    wallet_short_part = 0
    bill_change_part = 0
    if bill[0] > bill[1]:
        bill_long_part = bill[0]
        bill_short_part = bill[1]
    else:
        bill_long_part = bill[1]
        bill_short_part = bill[0]
    
    if wallet[0] > wallet[1]:
        wallet_long_part = wallet[0]
        wallet_short_part = wallet[1]        
    else:
        wallet_long_part = wallet[1]
        wallet_short_part = wallet[0]
    # print(bill_long_part, bill_short_part)
        
    while not ((bill_long_part <= wallet_long_part and bill_short_part <= wallet_short_part) or (bill_short_part <= wallet_long_part and bill_long_part <= wallet_short_part)):
        answer += 1
        bill_change_part = bill_long_part // 2
        if bill_short_part > bill_change_part:
            (bill_long_part, bill_short_part) = (bill_short_part, bill_change_part)
        else:
            (bill_long_part, bill_short_part) = (bill_change_part, bill_short_part)
    
    return answer