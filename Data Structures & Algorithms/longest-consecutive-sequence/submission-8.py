class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Solution: go over all the numbers and check if it's the starter
        #by checking if n - 1 is in the list. If it is, initialize length
        #and check if the next number exists. return length
        numSet = set(nums)
        longest = 0
        for n in numSet:
            if (n - 1 not in numSet):
                length = 1
                while (n + length in numSet):
                    length += 1
                longest = max(longest, length)
        return longest