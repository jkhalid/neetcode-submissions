class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        up , down , left, right = 0, len(matrix)-1, 0, len(matrix[0]) -1
        row = 0

        while up <= down:
            mid = (up + down) // 2
            if target < matrix[mid][0]:
                down = mid -1
            elif target > matrix[mid][-1]:
                up = mid + 1
            else:
                row = mid
                break
            
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] > target:
                right = mid -1
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                return True
        return False
        