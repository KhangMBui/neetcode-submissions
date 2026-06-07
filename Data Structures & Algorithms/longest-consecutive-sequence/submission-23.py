class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Solution: Create a numset out of nums, find
        # the starter number and start counting
        
        longest = 0
        for n in nums:
            if (n - 1 not in nums):
                length = 1
                while (n + length in nums):
                    length += 1
                longest = max(longest, length)
        return longest