class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # target = 7, [2, 3, 1, 2, 4, 3]
        # l, r
        # [2, 3] = 5
        # [2, 3, 1] = 6
        # [2, 3, 1, 2] = 7, collect size
        # now shrink l: [3, 1, 2] = 6, decide to keep expanding r
        # [3, 1, 2, 4]: 10, collect size
        # now shirnk l: [1, 2, 4] = 7, collect size
        # now shrink l: [2, 4], decide to keep expanding r
        # [2, 4, 3] = 9, collect size
        # now shrink l: [4, 3] = 7. Collect size

        if not nums:
            return -1
        
        l = 0
        curr_sum = 0
        res = float("inf")

        for r in range(len(nums)):
            curr_sum += nums[r]
            while curr_sum >= target:
                res = min(res, r - l + 1)
                curr_sum -= nums[l]
                l += 1
        # Space: O(1), time: O(n)
        return res if res != float("inf") else 0