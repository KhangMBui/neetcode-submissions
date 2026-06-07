class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        #Solution: calculate prefix and postfix in 2 iterations
        #and multiply them together
        #Calculate prefix:
        # [1, 1, 1, 1]
        # [1, 2, 4, 6] => [1, 1, 2, 8]
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        #Calculate postfix and put them into the final result
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res