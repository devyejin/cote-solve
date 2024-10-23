from collections import deque

def solution(s):
    dq = deque()
    
    for char in s:
        if char == '(':
            dq.append(')')
        elif char == ')':
            if not dq or dq.popleft() != ')': #비어있거나 ')' 가 아니라면
                return False
    
    return not dq #비었으면 False로 평가됨
