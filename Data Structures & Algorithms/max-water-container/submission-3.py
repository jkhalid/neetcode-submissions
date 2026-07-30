class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l,r = 0, len(heights)-1
        max_area = 0

        while l < r:
            temp_area = min(heights[l], heights[r]) * (r-l)
            max_area = max(temp_area, max_area)

            if heights[l] > heights[r]:
                r-=1
            elif heights[l] < heights[r]:
                l+=1
            else:
                l+=1
                r-=1
        return max_area
        