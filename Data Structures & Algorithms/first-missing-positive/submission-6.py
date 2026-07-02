class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Achieve O(1) space without soring by using the 
        # input array itself as a hash map.

        # Idea: use the sign of each element as a flag. 
        # If nums[i] is negative, it means i + 1 exists in the array

        # [-2, -1, 0] -> [-4, -4, -4]
        if not nums:
            return -1
        
        n = len(nums)
        
        # Mark all negative numbers 0
        # Use index to actually modify the array
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        for num in nums:
            val = abs(num)

            # Only value from 1 -> n matter
            if 1 <= val <= n:
                index = val - 1

                if nums[index] > 0:
                    nums[index] *= -1
                
                if nums[index] == 0:
                    nums[index] = -(n + 1) # fake negative marker

        # Now iterate through the array
        for i in range(n):
            # The missing number is index at first non-negative value
            if nums[i] >= 0:
                return i + 1
        
        # If 1 through n all exists, answer is n + 1
        return n + 1