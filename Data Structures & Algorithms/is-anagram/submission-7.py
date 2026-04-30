class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slen = len(s)
        tlen = len(t)

        if slen != tlen:
            return False
        counts = [0] * 26
        ord_a = ord('a')
        for i in range(slen):
            counts[ord(s[i])-ord_a] +=1
            counts[ord(t[i])-ord_a] -=1
        
        for check in range(26):
            if counts[check] != 0:
                return False
        return True
