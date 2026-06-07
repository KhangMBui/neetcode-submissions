class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in numSet:
            if (n - 1 not in numSet):
                nextNumber = n + 1
                length = 1
                while (nextNumber in numSet):
                    length += 1
                    nextNumber += 1
                longest = max(longest, length)
        return longest