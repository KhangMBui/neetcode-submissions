class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Solution: Create a hashset to keep track of it
        isDuplicate = set()
        for n in nums:
            if (n in isDuplicate):
                return True
            isDuplicate.add(n)
        return False