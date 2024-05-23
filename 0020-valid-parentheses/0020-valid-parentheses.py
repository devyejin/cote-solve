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
            elif not stack or stack.pop() != char: # 빈 list False로 평가
                return False
        return not stack