class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #prefix postfix
        res = [1] * len(nums)
        #initialize the prefix arr:
        for i in range(1, len(nums)):
            res[i] = nums[i - 1] * res[i - 1]
        print(res)
        #calculate postfix:
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res