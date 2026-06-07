class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Solution: Make a set out of nums
        # find the starter number in the list
        # and start counting
        numset = set(nums)
        longest = 0
        for n in numset:
            if (n - 1 not in numset):
                length = 1
                while (n + length in numset):
                    length += 1
                longest = max(longest, length)
        return longest
        