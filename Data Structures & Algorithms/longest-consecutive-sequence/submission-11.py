class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Solution: go over the list and check if n - 1 exists
        #if not, it's a starter. Start counting length 
        numSet = set(nums)
        longest = 0
        for n in numSet:
            if (n - 1 in numSet):
                continue
            length = 1
            while ( n + length in numSet):
                length += 1
            longest = max(longest, length)
        return longest