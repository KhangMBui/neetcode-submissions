class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        k %= len(nums)

        def reverse(l: int, r: int) -> None:
            while l < r :
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        # Reverse whole array
        reverse(0, len(nums) - 1)
        # Now reverse first k elements:
        reverse(0, k - 1)
        # Now reverse the remaining
        reverse(k, len(nums) - 1)
        
        # 1 2 3 4 5 6 7 -> 5 6 7 1 2 3 4
        # 7 6 5 4 3 2 1 -> 5 6 7 4 3 2 1 -> 5 6 7 1 2 3 4