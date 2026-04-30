class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = len(board)
        cols = len(board[0])

        check_row = defaultdict(set)
        check_col = defaultdict(set)
        check_sq = defaultdict(set)

        for r in range (rows):
            for c in range (cols):
                if board[r][c] == '.':
                    continue
                if board[r][c] in check_row[r] or board[r][c] in check_col[c] or board[r][c] in check_sq[(r//3, c//3)]:
                    return False
                check_row[r].add(board[r][c])
                check_col[c].add(board[r][c])
                check_sq[(r//3, c//3)].add(board[r][c])
        return True

