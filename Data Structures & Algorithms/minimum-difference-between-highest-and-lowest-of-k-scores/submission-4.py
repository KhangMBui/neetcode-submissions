class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # [2, 5, 3, 1, 6, 3] => [1, 2, 3, 3, 5, 6]
        if not nums:
            return -1
        
        nums.sort()
        # Sorted => min will be l and max will be r (k)
        l = 0
        res = float("inf")
        for r in range(k - 1, len(nums)):
            while l <= r and r - l + 1 > k:
                l += 1
            res = min(res, nums[r] - nums[l])

        return res if res != float("inf") else 0
        