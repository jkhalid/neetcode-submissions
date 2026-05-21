class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)

        longest = 0
        
        for i in range(len(nums)):
            check = nums[i]+1
            while check in nums_set:
                check+=1
            longest = max(longest, check-nums[i])
        return longest