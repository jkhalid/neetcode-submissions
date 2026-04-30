class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        all_mutiplied = 1
        zero_count = 0
        for num in nums:
            if num:
                all_mutiplied *= num
            else:
                zero_count +=1     
        if zero_count > 1: return [0] * len(nums)
        res = [0] * len(nums)
        for i, num in enumerate(nums):
            if zero_count: res[i] = 0 if num else all_mutiplied
            else: res[i] = all_mutiplied // num
        return res
        