class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefixSum = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        for row in range(len(matrix)):
            self.prefixSum[row][0] = matrix[row][0]
            for col in range(1, len(matrix[0])):
                self.prefixSum[row][col] = self.prefixSum[row][col - 1] + self.matrix[row][col]

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
            if col1 > 0:
                res += self.prefixSum[r][col2] - self.prefixSum[r][col1 - 1]
            else:
                res += self.prefixSum[r][col2]
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)