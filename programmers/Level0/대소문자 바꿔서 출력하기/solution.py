str = input()
answer = ""
for i in range(len(str)):
    if str[i].islower():
        answer += str[i].upper()
    else:
        answer += str[i].lower()
print(answer)