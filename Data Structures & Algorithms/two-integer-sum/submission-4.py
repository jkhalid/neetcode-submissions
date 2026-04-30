class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        complements = {}

        for i,num in enumerate(nums):
            comp = target - num
            if comp in complements:
                val = complements[comp]
                return [val, i]
            complements[num] = i
        return [-1, -1]

