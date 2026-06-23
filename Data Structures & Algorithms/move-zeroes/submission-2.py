class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        
        l = 0

        for r in range(1, len(nums)):
            # We must first make sure nums[l] is a zero
            while l < r and nums[l] != 0:
                l += 1

            # If nums[r] is non-zero and nums[l] is zero, swap:
            if nums[r] != 0 and nums[l] == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
