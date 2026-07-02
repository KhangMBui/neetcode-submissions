class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Unsorted int array
        # Return SMALLEST positive interger not in nums

        if not nums:
            return -1
        
        min_val = min(nums)
        max_val = max(nums)

        is_positive = False

        if min_val > 0:
            min_val = 1

        for num in range(min_val, max_val + 1):
            if num >= 0:
                is_positive = True
            if num not in nums and num > 0:
                return num
        
        if not is_positive:
            return 1
        return max_val + 1

