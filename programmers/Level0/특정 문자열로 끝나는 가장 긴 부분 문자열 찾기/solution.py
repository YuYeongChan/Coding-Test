def solution(myString, pat):
    answer = ''
    st = ""
    pa = ""
    for i in range(len(myString) - 1, -1, -1):
        st += myString[i]
    for i in range(len(pat) - 1, -1, -1):
        pa += pat[i]
    if pa in st:
        a = st.index(pa)
    # print(a)
    for i in range(len(myString) - a):
        answer += myString[i]
    return answer