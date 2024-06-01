class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for char in s:
            if char == '(':
                stack.append(')')
            elif char == '{':
                stack.append('}')
            elif char == '[':
                stack.append(']')
            elif stack.pop() != char or not stack: # 빈 list False로 평가
                return False
        return not stack