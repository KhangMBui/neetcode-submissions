class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        def find_first() -> int:
            l, r = 0, len(nums) - 1
            res = -1
            while l <= r:
                m = (r + l) // 2
                if nums[m] < target:
                    l = m + 1
                elif nums[m] > target:
                    r = m - 1
                else:
                    res = m # Save the index
                    r = m - 1 # Keep searching left
            return res
    
        def find_last() -> int:
            l, r = 0, len(nums) - 1
            res = -1
            while l <= r:
                m = (r + l) // 2
                if nums[m] < target:
                    l = m + 1
                elif nums[m] > target:
                    r = m - 1
                else:
                    res = m # Save the index
                    l = m + 1 # Keep searching left
            return res
        
        return [find_first(), find_last()]