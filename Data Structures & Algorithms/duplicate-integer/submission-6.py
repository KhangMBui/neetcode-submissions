class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set()
        for n in nums:
            if (n not in unique):
                unique.add(n)
            else:
                return True
        return False