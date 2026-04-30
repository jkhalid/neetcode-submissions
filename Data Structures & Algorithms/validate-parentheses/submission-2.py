class Solution:
    def isValid(self, s: str) -> bool:

        opening = ['(','{', '[']
        closing = [')', '}', ']']

        stack = []

        for char in s:
            if char in opening:
                stack.append(char)  
            elif char in closing and stack:
                val = stack.pop()
                if opening.index(val) != closing.index(char):
                    return False
            else:
                return False        
        return True if not stack else False