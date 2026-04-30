class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        comps = {}

        for i in range(len(nums)):
            if nums[i] in comps:
                return [comps[nums[i]], i]
            else:
                comp = target - nums[i]
                comps[comp] = i
        return null
        