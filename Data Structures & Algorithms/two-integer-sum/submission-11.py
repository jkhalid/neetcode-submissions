class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        complements = {}

        for index,num in enumerate(nums):
            comp = target - nums[index]

            if comp in complements:
                return [complements[comp], index]
            else:
                complements[num] = index
        return []

        