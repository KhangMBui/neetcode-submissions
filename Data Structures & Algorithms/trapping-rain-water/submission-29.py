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
        max_l = max_r = 0
        res = 0

        while l < r:
            max_l = max(max_l, height[l])
            max_r = max(max_r, height[r])

            if max_l < max_r:
                # max_l is smaller => left wall is the limiting wall, define the water trapped in height[l]
                res += max_l - height[l]
                l += 1
            else:
                res += max_r - height[r]
                r -= 1
        return res
            

        