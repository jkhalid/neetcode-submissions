class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) -1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid +1
        
        true_left = left

        left, right = 0 , len(nums) -1

        if target >= nums[true_left] and target <=nums[right]:
            left = true_left
        else:
            right = true_left -1
        
        while left <= right:
            mid  = (left + right) // 2
            if nums[mid] > target:
                right = mid -1
            elif nums[mid] < target:
                left = mid +1
            else:
                return mid
        return -1

