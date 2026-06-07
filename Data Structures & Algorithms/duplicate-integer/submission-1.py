class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numberSet = set()
        for n in nums:
            if n in numberSet:
                return True
            else:
                numberSet.add(n)
        return False