class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Return true if there exists i and j such that
        # nums[i] == nums[j] and abs(i - j) <= k
        # Could I store it in a set? a tuple of (value, index)?

        if not nums:
            return False

        seen = set()
        l = 0

        for r in range(len(nums)):
            while abs(r - l) > k:
                seen.remove(nums[l])
                l += 1
            
            if nums[r] in seen and abs(r - l) <= k:
                return True
            seen.add(nums[r])
            
        return False