class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        rows = len(matrix)
        cols = len(matrix[0]) - 1

        for i in range(rows):
            if matrix[i][0] <= target <= matrix[i][cols]:
                low, high = 0, cols
                while low <= high:
                    mid = (low + high) // 2
                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] > target:
                        high = mid - 1
                    else:
                        low = mid + 1
        return False
        
       
        