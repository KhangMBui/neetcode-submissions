class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            # The water level is limited by the shorter bar.
            # Area = width * min(left height, right height)
            curr_area = (r - l) * min(heights[l], heights[r])
            res = max(res, curr_area)

            # Move the pointer at the shorter bar inward.
            # Why?
            # - The current area is limited by the shorter side.
            # - If we move the taller bar inward, the width gets smaller
            #   and the limiting height stays the same or becomes even worse,
            #   so the area cannot improve.
            # - But if we move the shorter bar inward, we may find a taller bar,
            #   which could increase the limiting height enough to produce a larger area.
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res