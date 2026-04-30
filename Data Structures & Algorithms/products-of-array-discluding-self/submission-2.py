class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # prefix postfix concept

        result = [1] * len(nums)

        prefix = 1

        for i, n in enumerate(nums):
            result[i] = prefix
            prefix *= n
        
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result 
        