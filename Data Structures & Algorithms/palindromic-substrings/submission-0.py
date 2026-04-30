class Solution:
    def countSubstrings(self, s: str) -> int:

        total = 0
        
        for i in range(len(s)):

            counter = 0
            l, r = i, i 
            
            while l >=0 and r <len(s) and s[l] == s[r]:
                counter+=1
                l-=1
                r+=1
            l, r = i, i+1 
            while l >=0 and r <len(s) and s[l] == s[r]:
                counter+=1
                l-=1
                r+=1
            total +=counter
        return total
            
            

        