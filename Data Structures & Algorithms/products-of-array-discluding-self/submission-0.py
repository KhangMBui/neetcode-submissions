class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # solution: create two arrays, prefix and postfix, of the current array
        # and multiply them together into 1 new array
        prefix, postfix = [None]*len(nums), [None]*len(nums)
        prefix[0] = nums[0]
        postfix[len(postfix) - 1] = nums[len(nums) - 1]
        #prefix
        for i in range(1, len(nums)):
            prefix[i] = nums[i] * prefix[i-1]
        print(prefix)
        #postfix
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = nums[i] * postfix[i+1]
        print(postfix)
        res = [None]*len(nums)
        for i in range(len(prefix)):
            if (i == 0):
                res[i] = 1 * postfix[i + 1]
            elif (i == len(prefix) - 1):
                res[i] = prefix[i - 1]
            else:
                res[i] = prefix[i - 1] * postfix[i + 1]
        return res