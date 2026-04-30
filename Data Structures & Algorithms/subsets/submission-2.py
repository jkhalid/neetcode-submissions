class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []
        curr_set = []

        def helper(i):
            if i >= len(nums):
                result.append(curr_set.copy())
                return
            
            curr_set.append(nums[i])
            helper(i+1)

            curr_set.pop()
            helper(i+1)


        helper(0)
        return result
        