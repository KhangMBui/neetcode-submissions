class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # return perimeter of the island
        # perimeter of a block is 4
        # However, if blocks are adjacent to each other,
        # only the, I could see its perimeter is (4 - how many blocks it's adjecent to)
        # So for each block adjacent, minus 1 in its total parameter
        # For example: 
        #  grid = [
        #     [1,1,0,0],
        #     [1,0,0,0],
        #     [1,1,1,0],
        #     [0,0,1,1]
        # ]
        # Perimeter = 3 + 2 + 2 + 2 + 2 + 2 + 2 + 3

        if not grid or not grid[0]:
            return -1
        
        rows, cols = len(grid), len(grid[0])

        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        res = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res += 4
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if (
                            0 <= nr < rows and
                            0 <= nc < cols and 
                            grid[nr][nc] == 1
                        ):
                            res -= 1

        return res



