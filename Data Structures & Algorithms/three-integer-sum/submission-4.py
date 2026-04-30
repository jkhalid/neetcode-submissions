class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        n = len(nums)-1
        results = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            start = i+1
            end = n

            while start < end:
                three_sum = nums[i] + nums[start] + nums[end]

                if three_sum < 0:
                    start +=1
                elif three_sum > 0:
                    end-=1
                else:
                    results.append([nums[i], nums[start],nums[end]])
                    start+=1
                    end-=1
                    while nums[start] == nums[start - 1] and start < end:
                        start += 1
        return results

        