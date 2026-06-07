class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Solution 1: Hashset
        if not nums:
            return -1
        seen = set()
        for n in nums:
            if n in seen:
                return n
            seen.add(n)
        return -1