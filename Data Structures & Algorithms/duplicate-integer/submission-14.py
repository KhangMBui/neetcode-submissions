class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        unique = set()

        for n in nums:
            if n in unique:
                return True
            unique.add(n)
        return False