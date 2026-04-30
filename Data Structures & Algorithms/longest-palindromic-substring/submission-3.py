class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        resIdx = 0
        resLen = 0
        # using dynamic programming

        for i in range(n):
            # odd number
            l, r = i, i
            while l >= 0 and r < n and s[l]==s[r]:
                if (r-l+1) > resLen:
                    resIdx = l
                    resLen = r-l+1
                l-=1
                r+=1
            
            # even number
            l, r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                if (r-l+1) > resLen:
                    resIdx = l
                    resLen = r-l+1
                l-=1
                r+=1
        return s[resIdx : resIdx + resLen]

        