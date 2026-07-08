class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        n_s = len(s)
        n_t = len(t)

        if n_s != n_t:
            return False
        
        check = [0] * 26

        for i in range(n_s):
            val_s = ord(s[i]) - ord('a')
            val_t = ord(t[i]) - ord('a')

            check[val_s]+=1
            check[val_t]-=1
        
        for i in range(26):
            if check[i] != 0:
                return False
        return True
        