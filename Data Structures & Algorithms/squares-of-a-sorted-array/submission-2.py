class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # [-4, -1, 0, 3, 10]
        # [0, 1, 9, 16, 100]
        # Since the array is sorted, the largest numbers
        # will be at one of the 2 ends.
        # Since the problem does not ask to modify the array
        # in place, we could put the result in a separate array
        if not nums:
            return []
        
        l, r = 0, len(nums) - 1
        res = []
        while l <= r:
            square_l = nums[l] ** 2
            square_r = nums[r] ** 2
            if square_l > square_r:
                res.insert(0, square_l)
                l += 1
            else:
                res.insert(0, square_r)
                r -= 1
        return res

