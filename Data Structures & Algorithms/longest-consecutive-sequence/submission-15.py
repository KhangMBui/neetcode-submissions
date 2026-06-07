class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Solution: create a set for the list nums. Go
        #over the set and find a starter number. Start
        #counting forward and compare with longest
        longest = 0
        numSet = set(nums)
        for n in nums:
            if ( n - 1 in numSet):
                continue
            length = 1
            while (n + length in numSet):
                length += 1
            longest = max(longest, length)
        return longest