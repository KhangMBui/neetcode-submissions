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

        # Replace all negative numbers with 0
        # Must use index to actually modify the array
        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0
        
        # Use sign marking to record which values exists
        # Negative means that value exists
        for num in nums:
            val = abs(num)

            # Only values from 1 to n matter
            if 1 <= val <= n:
                index = val - 1

                # Mark that val exists by making nums[index] negative
                if nums[index] > 0:
                    nums[index] *= -1
                    
                elif nums[index] == 0: # if that number is 0, 
                    nums[index] = - (n + 1) # use a fake negative number
        
        # Find first index that was never marked
        for i in range(n):
            if nums[i] >= 0:
                return i + 1
        
        return n + 1
