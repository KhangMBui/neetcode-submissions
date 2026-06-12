class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return 0
        unique = set()
        for n in nums:
            if n in unique:
                return n
            unique.add(n)
        