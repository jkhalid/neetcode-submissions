class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        check = set()
        seen = set()



        for num in nums:
            check.add(num)
        longest = 1
        for num in nums:
            temp = 1
            if num in seen:
                continue
            while num+1 in check:
                temp+=1
                seen.add(num+1)
                num+=1
            longest = max(longest,temp)
        return longest
        
        