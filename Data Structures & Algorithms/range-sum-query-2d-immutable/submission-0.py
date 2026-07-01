class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Need to calculate sum within the rectangle defined by
        # upper left corner of (row1, col1) 
        # and then lower right corner of (row2, col2)

        if not self.matrix or not self.matrix[0]:
            print("Invalid matrix")
            return -1

        rows, cols = len(self.matrix), len(self.matrix[0])
        if not (
            0 <= row1 < rows and
            0 <= row2 < rows and
            0 <= col1 < cols and
            0 <= col2 < cols
        ):
            print("Invalid parameter coordinates")
            return -1
        
        # Calculate sum
        res = 0

        for r in range(row1, row2 + 1):
            for c in range(col1, col2 + 1):
                res += self.matrix[r][c]
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)