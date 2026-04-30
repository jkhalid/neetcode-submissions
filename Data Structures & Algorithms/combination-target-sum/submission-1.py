class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        result = []

        def helper(i, subset, total):
            if total == target:
                result.append(subset.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            subset.append(nums[i])
            helper(i, subset, total+nums[i])
            subset.pop()
            helper(i+1, subset, total)

        helper(0, [], 0)
        return result

