class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        
        longest = 0

        check = set(nums)

        for num in nums:
            if num-1 in check:
                continue
            length = 1
            while num+1 in check:
                length+=1
                num+=1
            longest = max(length, longest)
        
        return longest