class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        window_size = len(s1)

        l = 0

        s1_dict = defaultdict(int)
        for char in s1:
            s1_dict[char] +=1

        s2_dict = defaultdict(int)    

        for r in range(len(s2)):
            s2_dict[s2[r]] +=1

            if (r-l+1) == window_size:
                if s1_dict == s2_dict:
                    return True
                s2_dict[s2[l]] -=1
                if s2_dict[s2[l]] == 0:
                    del s2_dict[s2[l]]
                l+=1
        return False
        