class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Return true if there exists i and j such that
        # nums[i] == nums[j] and abs(i - j) <= k
        # Could I store it in a set? a tuple of (value, index)?

        if not nums:
            return False

        seen = {}

        for i, n in enumerate(nums):
            if n in seen and abs(i - seen[n]) <= k:
                return True
            seen[n] = i
        
        return False