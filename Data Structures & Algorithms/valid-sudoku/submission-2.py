class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

       check_cols = defaultdict(set)
       check_rows = defaultdict(set)
       check_squares = defaultdict(set) 


       for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            if (board[r][c] in check_rows[r] 
                or board[r][c] in check_cols[c] 
                or board[r][c] in check_squares[(r // 3, c // 3)]):
                return False
            check_cols[c].add(board[r][c])
            check_rows[r].add(board[r][c])
            check_squares[(r // 3, c // 3)].add(board[r][c])

       return True

        