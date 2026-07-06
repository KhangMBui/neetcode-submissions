class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        
        # [3, 4, 4, 5, 6, 1, 2, 2], target = 1
        # l = 0, r = 7, m = 3. left sorted half, move rightward
        
        n = len(nums)
        l, r = 0, n - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return True

            # if landed in left sorted half
            if (nums[l] < nums[m]):
                # Let's see where the target lies in
                # If it's in the left sorted half
                if (nums[l] <= target < nums[m]):
                    r = m - 1 # push leftward to find target
                else:
                    l = m + 1
            # if landed in right sorted half
            elif nums[l] > nums[m]:
                # If it's in the right sorted half
                if (nums[m] < target <= nums[r]):
                    l = m + 1 # push rightward to find target
                else:
                    r = m - 1
            # In spots where duplicates are there
            # Cannot tell which side is sorted => increment left and try again
            else:
                l += 1
        return False