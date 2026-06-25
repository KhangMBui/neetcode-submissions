class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return [-1, -1]

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            # If not equal, then
            # if m is bigger than l => left half sorted
            # if m is smaller than r => right half sorted

            # Left half is sorted
            if nums[l] <= nums[m]:
                # Target is inside left sorted half
                if nums[l] <= target < nums[m]:
                    r = m - 1 # Search backwards
                else:
                    l = m + 1
            
            # Right half is sorted
            elif nums[l] > nums[m]:
                # Target is inside right sorted half
                if nums[m] < target <= nums[r]:
                    l = m + 1 # Search forwards
                else:
                    r = m - 1
        
        return -1

        