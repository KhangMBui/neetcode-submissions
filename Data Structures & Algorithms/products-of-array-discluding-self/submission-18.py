class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Given arr: [1, 2, 4, 6]
        # Prefix: [1, 1, 2, 8]
        # Suffix: [48, 24, 6, 1]
        # Prefix * Suffix = [48, 24, 12, 8] = result

        if not nums:
            return []

        products = [1] * len(nums)

        for i in range(1, len(nums)):
            products[i] = products[i - 1] * nums[i - 1]
        
        postfix = 1

        for i in range(len(nums) - 1, -1, -1):
            products[i] *= postfix
            postfix *= nums[i]
        return products


        