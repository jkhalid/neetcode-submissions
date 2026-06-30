class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        product = 1
        has_zero = 0
        has_zero_index = 0
        result = [0] * n
        for i in range(n):
            if nums[i] == 0 and has_zero == 1:
                return result;
            elif nums[i] == 0:
                has_zero +=1
                has_zero_index = i
            else:
                product *= nums[i]
        
        if has_zero == 1:
            result[has_zero_index] = product
            return result
        
        for i, num in enumerate(nums):
            result[i] = product//num
        return result