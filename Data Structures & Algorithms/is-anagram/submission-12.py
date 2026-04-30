class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        check =[0] * 26

        for c in s:
            val = ord(c) - ord('a')
            check[val] +=1
        
        for c in t:
            val = ord(c) - ord('a')
            check[val] -=1
        
        for val in check:
            if val != 0:
                return False
        return True
        