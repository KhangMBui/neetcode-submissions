class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniques = set()
        for number in nums:
            if (number not in uniques):
                uniques.add(number)
            else:
                return True
        return False
        