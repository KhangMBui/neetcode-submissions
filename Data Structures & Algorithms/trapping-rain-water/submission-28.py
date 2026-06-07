class Solution:
    def trap(self, height: List[int]) -> int:
        # Formula to calculate water trapped at position i:
        # min(height[l], height[r]) - height[i]

        # [0,2,0,3,1,0,1,3,2,1]

        # algorithm overview:
        # Iterate through the array
        # For each of the item, we'll find a valid right. 
        #   Basically march r forward until height[r] > height[l] (so it's able to trap water)
        # Then perform the formula min(height[l], height[r]) - height[i]
        # But in case at index 5, that won't work
        
        # For each position, we need to know:
        #   tallest bar seen so far from the left
        #   tallest bar seen so far from the right

        # Second approach: two pointers
        # at any pointer, the water trapped at i is determined by the smaller side:
            # if left_max < right_max => left_max is the limiting wall
            # if right_max < left_max => right_max is the limiting wall
        # So instead of precomputing all maxes, we keep:
            # l, r pointers
            # left_max, right_max

        if not height:
            return 0
        
        l, r = 0, len(height) - 1
        left_max = right_max = 0
        res = 0

        while l < r:
            left_max = max(left_max, height[l])
            right_max = max(right_max, height[r])

            if left_max < right_max:
                # left_max is the smaller wall, so water at l depends on left_max
                res += left_max - height[l]
                l += 1
            else: 
                # right_max is the smaller wall, so water at r depends on right_max
                res += right_max - height[r]
                r -= 1
        return res
            

        