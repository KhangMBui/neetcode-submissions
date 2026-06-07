class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Solution: Negative index marking. Every
        # number in the array points to another number
        # if we use abs
        if not nums:
            return -1
        for n in nums:
            idx = abs(n) - 1
            if nums[idx] > 0:
                nums[idx] *= - 1
            else:
                return abs(n)
        return -1