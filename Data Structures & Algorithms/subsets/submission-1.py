class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []
        curr_set = []

        def helper(i, curr_set):
            if i >= len(nums):
                result.append(curr_set.copy())
                return
            
            curr_set.append(nums[i])
            helper(i+1, curr_set)

            curr_set.pop()
            helper(i+1, curr_set)


        helper(0, curr_set)
        return result
        