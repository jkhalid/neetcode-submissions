class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []
        curr_set = []

        def helper(i, nums, curr_set, result):
            if i >= len(nums):
                result.append(curr_set.copy())
                return
            
            curr_set.append(nums[i])
            helper(i+1, nums, curr_set, result)

            curr_set.pop()
            helper(i+1, nums, curr_set, result)


        helper(0, nums, curr_set, result)
        return result
        