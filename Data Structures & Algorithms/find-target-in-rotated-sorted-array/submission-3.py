class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            # See if current position is in 
            # left sorted half or right sorted half

            if nums[m] >= nums[l]: # left sorted half
                # Target is inside left sorted half:
                if nums[l] <= target < nums[m]:
                    # Search leftward
                    r = m - 1
                else:
                    l = m + 1

            elif nums[m] < nums[l]: # right sorted half
                # Target is inside right sorted half
                if nums[m] < target <= nums[r]:
                    # search rightward
                    l = m + 1
                else:
                    r = m - 1
        return -1
