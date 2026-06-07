class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Solution 2
        if not nums:
            return -1
        for i in range(len(nums)):
            # Index marking:
            idx = abs(nums[i]) - 1
            if nums[idx] > 0:
                nums[idx] *= -1
            elif nums[idx] < 0:
                return abs(nums[i])
        return -1
        