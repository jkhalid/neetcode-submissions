class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        check = set(nums)
        longest = 1
        for num in check:
            
            if num -1 in check:
                continue
            length = 1
            while num+1 in check:
                length+=1
                num+=1
            longest = max(longest,length)
        return longest
        
        