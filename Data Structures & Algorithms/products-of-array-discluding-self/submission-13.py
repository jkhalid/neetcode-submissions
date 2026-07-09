class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        count_zero = 0
        zero_index = -1
        product = 1
        n = len(nums)

        for i in range(n):
            if nums[i] == 0:
                count_zero+=1
                zero_index = i
            else:
                product *= nums[i]
        
        if count_zero == 1:
            result = [0] * n
            result[zero_index] = product
            return result
        if count_zero > 1:
            return [0]*n
        
        #result = [1] * n
        prefix = [1] * n
        postfix = 1#[1] * n

        for i in range(1,n):
            prefix[i] = prefix[i-1]*nums[i-1]
        
        for i in range(n-2,-1,-1):
            postfix *= nums[i+1]
            prefix[i] = prefix[i]*postfix
        
        # for i in range(n):
        #     result[i] = prefix[i] * postfix[i]
        
        return prefix




        