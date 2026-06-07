class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numberSet = set()
        for n in nums:
            if (n not in numberSet):
                numberSet.add(n)
            else:
                return True
        return False