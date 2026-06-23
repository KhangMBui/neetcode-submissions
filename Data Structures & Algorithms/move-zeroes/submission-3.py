class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        
        insert_pos = 0

        for r in range(len(nums)):
            if nums[r] != 0:
                nums[insert_pos], nums[r] = nums[r], nums[insert_pos]
                insert_pos += 1
