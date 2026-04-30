class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)
        sum_1 = sum(nums)
        sum_2 = (n * (n+1)) // 2
        return sum_2 - sum_1        