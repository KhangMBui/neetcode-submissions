class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Use DFS to traverse each group independently
        # Iterate through each cell of the grid,
        # when encounter 1, perform DFS starting at that cell
        # and recursively visit every other 1 that is reachable
        # During this process, we mark the visited 1 as 0 to ensure
        # we don't revisit them, as they belong to the same group

        if not grid or not grid[0]:
            return -1
        
        rows, cols = len(grid), len(grid[0])

        islands = 0 

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r: int, c: int) -> None:
            grid[r][c] = 0 # Mark as 0 so we don't visit it anymore
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows and
                    0 <= nc < cols and
                    grid[nr][nc] == "1"
                ):
                    dfs(nr, nc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    # Perform DFS
                    dfs(r, c)
                    # Increment island count
                    islands += 1
        return islands
        

