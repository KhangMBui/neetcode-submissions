class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # sr, sc = our starting position
        # image is a matrix, which we're supposed to change blocks with same color of starting pixels,
        # change it into color

        if not image:
            return []

        rows, cols = len(image), len(image[0])
        starting_color = image[sr][sc]
        
        # If new color is same as starting color, don't need to do anything
        # This prevents infinite recursion
        if starting_color == color:
            return image
        
        directions = [
            (0, -1), # left
            (0, 1), # right
            (-1, 0), # up
            (1, 0) # down
        ]

        def helper(sr, sc):
            # Change the current cell's color:
            image[sr][sc] = color
            # Recursive or iteratively spread the fill to neighboring cells
            for dir_r, dir_c in directions:
                next_r, next_c = sr + dir_r, sc + dir_c

                if 0 <= next_r < rows and 0 <= next_c < cols and image[next_r][next_c] == starting_color:
                    helper(next_r, next_c)
        
        helper(sr, sc)
        return image