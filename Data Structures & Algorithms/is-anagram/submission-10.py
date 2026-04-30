class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        if len_s != len_t:
            return False
        counts = [0] * 26
        ord_a = ord('a')
        for i in range(len_s):
            counts[ord(s[i])-ord_a]+=1
            counts[ord(t[i])-ord_a]-=1
        
        for check in counts:
            if check !=0:
                return False
        return True
        