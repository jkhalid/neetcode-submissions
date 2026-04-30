class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        cache = [[0] * n for _ in range(m)]

        def memoization(r, c):
            if r == m or c == n:
                return 0
            if cache[r][c] > 0:
                return cache[r][c]
            if r == m-1 or c == n-1:
                return 1
            
            cache[r][c] = memoization(r+1, c) + memoization(r, c+1)
            return cache[r][c]
        
        return memoization(0, 0)
        
        
        