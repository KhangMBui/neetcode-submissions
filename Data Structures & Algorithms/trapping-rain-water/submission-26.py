class Solution:
    def trap(self, height: List[int]) -> int:
        # Formula to calculate water trapped at position i:
        # min(height[l], height[r]) - height[i]

        # [0,2,0,3,1,0,1,3,2,1]

        # at index 0: nothing (we might start from index 1)
        # at index 1: 0 - 2 = -2 => negative. No water trapped
        # at index 2: 2 - 0 = 2 => positive. water trapped = 2
        # at index 3: 0 - 3 = -3 => negative. No water trapped
        # at index 4: wait, maybe we have to find a height[r] that is > height[i]

        # algorithm overview:
        # Iterate through the array
        # For each of the item, we'll find a valid right. 
        #   Basically march r forward until height[r] > height[l] (so it's able to trap water)
        # Then perform the formula min(height[l], height[r]) - height[i]
        # But in case at index 5, that won't work
        
        # For each position, we need to know:
        #   tallest bar seen so far from the left
        #   tallest bar seen so far from the right

        # One approach: precompute left max & right max arrays:
        # left_max = [0, 2, 2, 3, 3, 3, 3, 3, 3, 3]
        # right_max = [3, 3, 3, 3, 3, 3, 3, 3, 2, 1]

        # then for each number in [height]:
        # min(left_max[i], right_max[i]) - height[i]

        if not height:
            return 0
        
        res = 0

        max_l = float("-inf")
        max_left = []
        for h in height:
            max_l = max(h, max_l)
            max_left.append(max_l)
        
        max_r = float("-inf")
        max_right = []
        for h in height[::-1]:
            max_r = max(h, max_r)
            max_right.append(max_r)
        max_right.reverse()


        for i in range(len(height)):
            res += max(0, min(max_left[i], max_right[i]) - height[i])
        
        return res
        