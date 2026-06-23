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
            while nums[l] != 0 and l < r:
                l += 1
            if nums[r] == 0:
                continue
            # nums[r] != 0, a real number, we must move to where zero is, 
            # which should be l?
            # Let's assume that for now. We swap l and r
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
