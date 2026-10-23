class Solution:
    def isValid(self, s: str) -> bool:

        openB = ['[', '(', '{']
        closeB = [']',')','}']

        stack = []

        for b in s:
            if b in openB:
                stack.append(b)
            elif b in closeB:
                if stack:
                    val = stack.pop()
                    if closeB.index(b) != openB.index(val):
                        return False
                else:
                    return False
            else:
                return False

        if stack:
            return False
        return True
        