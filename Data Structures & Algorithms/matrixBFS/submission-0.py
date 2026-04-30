class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        visit = set()
        queue.append((0,0))
        visit.add((0,0))
        length = 0

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == rows-1 and c == cols-1:
                    return length
                
                directions = [[0,1], [1,0], [-1,0], [0,-1]]

                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if min(nr, nc) <0 or nr >=rows or nc>=cols or (nr,nc) in visit or grid[nr][nc] == 1:
                        continue
                    queue.append((nr,nc))
                    visit.add((nr,nc))
            length+=1
        return -1
        