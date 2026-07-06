class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [3, 4, 5, 6, 1, 2], l = 0, r = 5, m = 2, it's in the left sorted half
        # l = m + 1 = 3
        # [3, 4, 5, 6, 1, 2], l = 3, r = 5, m = 4, it's in the right sorted half.
        # here, we may need to update our result?, r  = m - 1 = 3 # keep going
        # [3, 4, 5, 6, 1, 2], l = 3, r = 3, m = 3. Left sorted half, move l forward...exit condition
        if not nums:
            return -1
        
        n = len(nums)
        l, r = 0, n - 1
        res = float("inf")

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
            m = (l + r) // 2
            res = min(res, nums[m])
            # If land in left sorted half
            if nums[l] <= nums[m]:
                # We need to go further to the right,
                # as it's where the right sorted half with min value is
                l = m + 1
            # If land in right sorted half
            else:
                r = m - 1
        return res