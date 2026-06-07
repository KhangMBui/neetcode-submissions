class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Solution: Binary search to find the row where it belongs
        # and then binary search that row to find the target element
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bot = 0, ROWS - 1
        while (top <= bot):
            midRow = (top + bot) // 2
            if (target > matrix[midRow][-1]):
                top = midRow + 1
            elif (target < matrix[midRow][0]):
                bot = midRow - 1
            else:
                break
        if not (top <= bot):
            return False
        midRow = (top + bot) // 2
        l, r = 0, COLS - 1
        while (l <= r):
            m = (l + r) // 2
            if (target > matrix[midRow][m]):
                l = m + 1
            elif (target < matrix[midRow][m]):
                r = m - 1
            else:
                return True
        return False