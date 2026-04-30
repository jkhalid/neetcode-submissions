class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        myset = set()

        for num in nums:
            myset.add(num)
        return not len(myset) == len(nums)

         