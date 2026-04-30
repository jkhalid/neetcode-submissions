class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1 for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i!=j:
                    result[i] *= nums[j]
        return result