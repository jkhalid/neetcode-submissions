class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        output = []
        for i in range(n):
            prod = 1
            for j in range(n):
                if i!=j:
                    prod = prod * nums[j]
            output.append(prod)
        return output
        