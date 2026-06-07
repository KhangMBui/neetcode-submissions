class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Solution: Negative indexing marking
        # Explanation: We can use the value of 
        # each number in nums to point to another 
        # number (and mark it negative) with the same algorithm.
        # If we reach a pointer number that is already negative,
        # we know that it's visited and therefore,
        # the number is duplicate
        if not nums:
            return -1
        for n in nums:
            idx = abs(n) - 1
            if (nums[idx] < 0):
                return abs(n)
            nums[idx] *= -1
        return -1