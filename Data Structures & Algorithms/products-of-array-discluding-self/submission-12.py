class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Solution: Prefix Postfix
        # [1, 2, 4, 6] => prefix = [1, 1, 2, 8]
        # [1, 2, 4, 6] => postfix = [48 ,24, 6, 1]
        # Result = postfix * prefix = [48, 24, 12, 8]
        res = [1]
        for i in range(1, len(nums)):
            res.append(nums[i - 1] * res[i - 1])
        postfix = 1
        for i in range(len(res) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res