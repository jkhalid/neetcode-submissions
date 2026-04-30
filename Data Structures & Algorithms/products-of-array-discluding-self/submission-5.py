class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        product = 1
        zero_count = 0
        n = len(nums)
        for num in nums:
            if num == 0:
                zero_count+=1
            else:
                product *= num
        result = [0 for _ in range(n)]
        if zero_count > 1:
            result
        elif zero_count == 1:
            for i in range(n):
                if nums[i] == 0:
                    result[i] = product
                    return result
        else:
            for i in range(n):
                result[i] = product // nums[i]
        return result

