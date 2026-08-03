class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = 0 
        r = n-1
        lmax = 0
        rmax = 0

        total = 0

        while l < r:
            if height[l] <= height[r]:
                lmax = max(lmax, height[l])
                total += lmax - height[l]
                l+=1
            else:
                rmax = max(rmax, height[r])
                total+= rmax - height[r]
                r-=1


        return total
        