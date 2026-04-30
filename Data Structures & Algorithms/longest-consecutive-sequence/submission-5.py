class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        check_set = set(nums)

        result = 0

        for num in check_set:
            i = 1
            while num + i in check_set:
                i+=1
            result = max(result, i)
        return result