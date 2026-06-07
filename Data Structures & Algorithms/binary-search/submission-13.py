class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Solution: formula to calculate middle index is l + (r - l) // 2
        # or (r + l) // 2 
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (r + l) // 2
            if (nums[m] > target):
                r = m - 1
            elif (nums[m] < target):
                l = m + 1
            else:
                return m
        return -1