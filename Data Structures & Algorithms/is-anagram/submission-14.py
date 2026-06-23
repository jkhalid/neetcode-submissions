class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        length = len(s)
        alpha = [0] * 26
        for i in range(length):
            val_s = ord(s[i]) - ord('a')
            val_t = ord(t[i]) - ord('a')

            alpha[val_s]+=1
            alpha[val_t]-=1
        
        for check in alpha:
            if check != 0:
                return False
            
        return True
