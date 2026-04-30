class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 0: return 0

        count = 1
        result = 0
        nums.sort()

        for i in range(1, n):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i - 1] + 1:
                    count +=1
                else:
                    result = max(count, result)
                    count = 1
        return max(count, result)
                
        