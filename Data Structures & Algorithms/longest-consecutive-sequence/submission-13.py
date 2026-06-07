class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Solution: Go over the number set, look for starter
        #and count length and compare with longest
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