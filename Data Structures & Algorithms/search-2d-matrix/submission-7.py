class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Solution: Perform binary search to find the right row
        # and then use binary search to find if target in that row
        top, bot = 0, len(matrix) - 1
        while ( top <= bot ):
            midRow = bot + (top - bot)// 2
            if (matrix[midRow][-1] < target):
                top = midRow + 1
            elif (matrix[midRow][0] > target):
                bot = midRow - 1
            else:
                break
        if (top > bot):
            return False
        midRow = bot + (top - bot)//2
        l, r = 0, len(matrix[0]) - 1
        while (l <= r):
            m = l + (r - l)//2
            if (matrix[midRow][m] > target):
                r = m - 1
            elif (matrix[midRow][m] < target):
                l = m + 1
            else:
                return True
        return False