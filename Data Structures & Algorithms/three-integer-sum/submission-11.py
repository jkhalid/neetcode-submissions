class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)-1
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            start = i+1
            end = n
            while start < end:
                sum_3 = nums[i] + nums[start] + nums[end]

                if sum_3 > 0:
                    end-=1
                elif sum_3 < 0:
                    start+=1
                else:
                    result.append([nums[i], nums[start], nums[end]])
                    start+=1
                    end-=1
                    while nums[start] == nums[start-1] and start < end:
                        start+=1
        return result