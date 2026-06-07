class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Solution: Prefix * Postfix
        #[1, 2, 4, 6] => [1, 1, 2, 8]
        res = [1]*len(nums)
        #Make prefix
        for i in range(1, len(nums)):
            res[i] = nums[i - 1] * res[i - 1]
        #Now multiply it with postfix:
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res