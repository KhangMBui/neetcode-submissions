class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numberList = []
        for n in nums:
            if n in numberList:
                return True
            else:
                numberList.append(n)
        return False