class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows = len(matrix)
        cols = len(matrix[0])

        up = 0
        down = rows-1
        row = 0

        while up <= down:
            mid = (up+down) // 2
            if target > matrix[mid][-1]:
                up = mid +1
            elif target < matrix[mid][0]:
                down = mid - 1
            else:
                row = mid
                break
        
        left, right = 0 , cols-1

        while left <= right:
            mid = (left + right) // 2
            if target > matrix[row][mid]:
                left = mid +1
            elif target < matrix[row][mid]:
                right = mid-1
            else:
                return True
        
        return False
