class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        check_row = set()
        check_col = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    check_row.add(i)
                    check_col.add(j)
        
        for row in check_row:
            for col in range(len(matrix[0])):
                matrix[row][col] = 0
        for row in range(len(matrix)):
            for col in check_col:
                matrix[row][col] = 0