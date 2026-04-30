class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        results = []
        n = len(nums) -1
        nums.sort()

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left = i+1
            right = n
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                if  three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    results.append([nums[i], nums[left],nums[right]])
                    left +=1
                    right -=1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return results
        