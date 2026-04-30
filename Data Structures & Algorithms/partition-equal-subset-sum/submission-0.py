class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums) % 2:
            return False
        
        memo = set()
        memo.add(0)
        target = sum(nums) // 2

        for i in range(len(nums)-1, -1, -1):
            nextdp = set()
            for num in memo:
                if nums[i] + num == target:
                    return True
                nextdp.add(nums[i] + num)
                nextdp.add(num)
            memo = nextdp
        return False

                
        