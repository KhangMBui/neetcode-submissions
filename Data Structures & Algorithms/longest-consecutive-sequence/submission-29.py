class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Solution: try to find a number that is a starter
        # and then count it up
        longest = 0
        if not nums:
            return 0
        for n in nums:
            if n - 1 in nums:
                continue
            length = 1
            while (n + length in nums):
                length += 1
            longest = max(longest, length)
        return longest