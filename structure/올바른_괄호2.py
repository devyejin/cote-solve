def solution(s):
    st = list()
    for char in s:
        if char == '(':
            st.append(char)
        elif char == ')':
            try:
                st.pop()
            except IndexError:
                return False
    
    return len(st) == 0