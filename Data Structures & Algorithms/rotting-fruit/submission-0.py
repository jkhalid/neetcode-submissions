class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        time = 0
        fresh = 0
        queue = deque()

        # first count the number of fresh oranges and construct queue with rotten ones
        for i in range(rows):   
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh+=1
                if grid[i][j] == 2:
                    queue.append((i,j))
        
        directions = [[0,1], [1,0], [-1,0], [0,-1]]
        while fresh > 0 and queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()

                for dr,dc in directions:
                    nr, nc = r+dr, c+dc
                    if (nr in range(rows) and nc in range(cols)) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr,nc))
                        fresh -=1
            time +=1
        return time if fresh == 0 else -1 
        