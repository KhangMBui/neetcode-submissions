class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Return true if there exists i and j such that
        # nums[i] == nums[j] and abs(i - j) <= k
        # Could I store it in a set? a tuple of (value, index)?

        if not nums:
            return False

        unique = set() # Set of (value, index)

        for i, n in enumerate(nums):
            for item in unique:
                if n == item[0]:
                    if abs(i - item[1]) <= k:
                        return True
            unique.add((n, i))
        
        return False