class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])
        directions = [[0,1], [1,0], [-1,0], [0,-1]]

        def findWord(r, c, i):
            if i == len(word):
                return True
            if min(r,c) < 0 or r >=rows or c>=cols or word[i] != board[r][c] or board[r][c] == '#':
                return False

            board[r][c] = '#'
            res = False
            for dr, dc in directions:
                res = res or findWord(r+dr, c+dc, i+1)
            board[r][c] = word[i]
            return res


        for i in range(rows):
            for j in range(cols):
                decision = findWord(i, j, 0)
                if decision:
                    return True
        return False
        