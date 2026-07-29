class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        if nums[0] > 0:
            return result
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            target = -1*nums[i]
            start = i+1
            two_sum_results = self.twoSum(nums, start, target)
            for res in two_sum_results:
                result.append([nums[i]] + res)
        return result
    
    def twoSum(self, nums: List[int], start: int, target: int) -> List[List[int]]:
        result = []
        left, right = start, len(nums) - 1
        while left < right:
            check = nums[left] + nums[right]
            if check == target:
                result.append([nums[left], nums[right]])
                left+=1
                while left < right and nums[left-1] == nums[left]:
                    left+=1
            elif check < target:
                left+=1
            else:
                right-=1
        return result

        

        