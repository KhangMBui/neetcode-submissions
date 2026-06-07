class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # We create a hashmap that sores number?
        # Actually hashset sounds better as to reduce duplicates
        # We'll find the starter number (the number that has no
        # number that's 1 unit smaller than it) and then trace
        # its path, counting longest path.
        if not nums:
            return 0
        longest = 0
        for i, n in enumerate(nums):
            if (n - 1) in nums:
                continue
            number = n
            length = 1
            while (number + 1) in nums:
                length += 1
                number += 1
            longest = max(longest, length)
        return longest
        