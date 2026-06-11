class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Could we simply have a result array to store max values?
        if not nums or k <= 0:
            return []
        
        res = []
        l, r = 0, k - 1

        while r < len(nums):
            res.append(max(nums[l : r + 1]))
            l += 1
            r += 1
        
        return res
