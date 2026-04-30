class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

     check_list = []

     for num in nums:
        if num in check_list:
            return True
        else:
            check_list.append(num)
    
     return False
         