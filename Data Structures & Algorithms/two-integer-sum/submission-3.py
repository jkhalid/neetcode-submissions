class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comps = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in comps:
                return [comps[complement], i]
            comps[num] = i
        return -1