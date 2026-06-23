class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Return true if there exists i and j such that
        # nums[i] == nums[j] and abs(i - j) <= k
        # Could I store it in a set? a tuple of (value, index)?

        if not nums:
            return False

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] == nums[j] and abs(i - j) <= k:
                    return True
        return False