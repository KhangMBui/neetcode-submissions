class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #prefix and postfix yes it is
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            res[i] = nums[i - 1] * res[i - 1]
        #now do postfix:
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res