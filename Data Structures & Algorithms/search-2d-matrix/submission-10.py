class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Solution: binary search to find the row the target is in
        # and then binary search that row to find the target
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bot = 0, len(matrix) - 1
        while (top <= bot):
            midRow = (top + bot)//2
            if (matrix[midRow][-1] < target):
                top = midRow + 1
            elif (matrix[midRow][0] > target):
                bot = midRow - 1
            else:
                break
        midRow = (top + bot)//2
        l, r = 0, len(matrix[midRow]) - 1
        while (l <= r):
            m = (l + r) // 2
            if (matrix[midRow][m] < target):
                l = m + 1
            elif (matrix[midRow][m] > target):
                r = m - 1
            else:
                return True
        return False