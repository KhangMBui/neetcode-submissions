class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Prefix, postfix
        prefix = [1]*len(nums)
        #prefix: [1, 1, 1, 1]
        #nums: [1, 2, 4, 6]
        #prefix => [1, 1, 2, 8]
        for i in range(1, len(prefix)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        #Now do postfix:
        postfix = 1
        for i in range(len(prefix) - 1, -1, -1):
            prefix[i] *= postfix
            postfix *= nums[i]
        return prefix
