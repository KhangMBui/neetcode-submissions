class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Figure out the longest consecutive sequence
        # Use a set to store each number
        # [2, 20, 4, 10, 3, 4, 5] => [2, 3, 4, 5, 10, 20]

        # Traverse through the nums again, find a number that (itself - 1) does not exist from the set -> starting point
        # Or maybe we check if (number - 1) exists in the set. If it doesn't => starting point
        # If it does => keep traversing
        # And then we keep looking for (number + 1) and add that to res with max(res, current)\

        if len(nums) == 0:
            return 0
        
        num_set = set(nums)

        res = 0

        for n in nums:
            if (n - 1) in num_set:
                continue
            
            # (We're only at this point when n is the starting number)
            # Found starting point, let's start counting
            count = 1
            while (n + count) in num_set:
                count += 1
            res = max(res, count)
        return res