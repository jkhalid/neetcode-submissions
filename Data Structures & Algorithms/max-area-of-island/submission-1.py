class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        max_area = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c)-> int:
            if min(r,c) < 0 or r >=rows or c>=cols or grid[r][c]==0:
                return 0
            grid[r][c] = 0
            area = 1
            area += dfs(r+1, c)
            area += dfs(r, c+1)
            area += dfs(r-1, c)
            area += dfs(r, c-1)
            return area


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i,j))
        return max_area