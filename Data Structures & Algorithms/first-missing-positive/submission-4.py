class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Achieve O(1) space without soring by using the 
        # input array itself as a hash map.

        # Idea: use the sign of each element as a flag. 
        # If nums[i] is negative, it means i + 1 exists in the arary
        if not nums:
            return -1
        
        # Replace all negative numbers with 0:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        for num in nums:
            val = abs(num)
            if 1 <= val <= len(nums):
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1 * (len(nums) + 1)
        
        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i
        
        return len(nums) + 1
