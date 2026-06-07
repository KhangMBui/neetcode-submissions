class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 2, 4, 6] => prefix: [1, 1, 2, 8]
        # postfix: [48, 24,6, 1]
        # prefix * postfix = [48, 24, 12, 8]
        if not nums:
            return []
        
        # Initialize prefix:
        products = [1] * len(nums)
        for i in range(1, len(nums)):
            products[i] = products[i - 1] * nums[i - 1]
        # [1, 1, 2, 8]
        # Calculate postfix
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            products[i] *= postfix
            postfix *= nums[i]
        return products