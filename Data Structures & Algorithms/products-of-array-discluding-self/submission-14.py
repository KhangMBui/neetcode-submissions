class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Solution: prefix postfix
        # Original: [1, 2, 4, 6]
        # Prefix: [1, 1, 2, 8]
        # Postfix: [48, 24, 6, 1]
        # Result = prefix * postfix = [48, 24, 12, 8]
        # Firstly, we need to create the prefix array:
        res = [1] * len(nums)
        # [1, 2, 4, 6]
        # [1, 1, 1, 1]
        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]
        postfix = 1
        # [1, 2, 4, 6]
        # [1, 1, 2, 8]
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

