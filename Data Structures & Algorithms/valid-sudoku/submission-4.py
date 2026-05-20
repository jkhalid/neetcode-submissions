class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        check_rows = defaultdict(set)
        check_cols = defaultdict(set)
        check_squares = defaultdict(set)

        rows = len(board)
        cols = len(board[0])

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == ".":
                    continue
                if(board[i][j] in check_rows[i]
                 or board[i][j] in check_cols[j]
                 or board[i][j] in check_squares[(i//3, j//3)]):
                 return False
                
                check_rows[i].add(board[i][j])
                check_cols[j].add(board[i][j])
                check_squares[(i//3, j//3)].add(board[i][j])
        return True

