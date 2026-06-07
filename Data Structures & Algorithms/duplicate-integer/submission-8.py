class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniques = set()
        for n in nums:
            if (n in uniques):
                return True
            uniques.add(n)
        return False