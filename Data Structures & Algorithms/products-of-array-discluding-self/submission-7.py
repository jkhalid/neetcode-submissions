class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        zero_index = 0
        zero_count = 0
        total_prod = 1
        n = len(nums)
        result = [0] * n
        for i,num in enumerate(nums):
            if num == 0:
                zero_index = i
                zero_count +=1
            else:
                total_prod *= num
        
        if zero_count > 1:
            return result
        if zero_count == 1:
            result[zero_index] = total_prod
        if zero_count == 0:
            for i in range(n):
                result[i] = total_prod // nums[i]
        return result



