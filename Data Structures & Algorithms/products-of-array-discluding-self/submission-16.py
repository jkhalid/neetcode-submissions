class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        count_zero = 0
        index = 0
        n = len(nums)
        for i,num in enumerate(nums):
            if num == 0:
                count_zero+=1
                index = i
            else:
                product *= num
        
        if count_zero == 1:
            result = [0] * n
            result[index] = product
            return result
        if count_zero > 1:
            result = [0] * n
            return result
        
        prefix = [1] * n
        postfix = [1] * n

        for i in range(1,n):
            prefix[i] = prefix[i-1]*nums[i-1]
        
        for i in range(n-2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i+1]
        
        result = [1] * n

        for i in range(n):
            result[i] = prefix[i] * postfix[i]
        
        return result


        