class Solution:
    def solve(self, board: List[List[str]]) -> None:


        rows, cols = len(board), len(board[0])
        flag = set()

        def dfs(r, c):
            if not(r in range(rows) and c in range(cols)) or board[r][c] != 'O' or (r, c) in flag:
                return
            
            flag.add((r, c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r in [0, rows-1] or c in [0, cols-1]):
                    dfs(r,c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r, c) not in flag:
                    board[r][c] = 'X'
         



