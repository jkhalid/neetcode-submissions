class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helper(subarr : List[int]) -> int:
            if not subarr:
                return 0
            if len(subarr) == 1:
                return subarr[0]
            dp = [0] * len(subarr)
            dp[0] = subarr[0]
            dp[1] = max(subarr[0], subarr[1])

            for i in range(2, len(subarr)):
                dp[i] = max(dp[i-1], subarr[i] + dp[i - 2])
            return dp[-1]
        
        if len(nums) == 1:
            return nums[0]

        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))    