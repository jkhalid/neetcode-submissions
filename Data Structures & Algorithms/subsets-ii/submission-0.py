class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        result = []
        curr_set = []

        def helper(i):
            if i >= len(nums):
                result.append(curr_set.copy())
                return
            
            curr_set.append(nums[i])
            helper(i+1)
            curr_set.pop()

            while i+1 <len(nums) and nums[i] == nums[i+1]:
                i+=1
            helper(i+1)
        
        helper(0)
        return result
        