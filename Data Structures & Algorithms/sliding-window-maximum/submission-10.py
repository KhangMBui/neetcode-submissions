class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # [1, 2, 1, 0, 4, 2, 6], k = 3
        # At 1 (window 1): q = [1]
        # At 2 (window 1 2): q = [2]
        # At 1 (window 1 2 1): q = [2, 1] => r = 3 => Output = [2], l = 1 (at 2)
        # At 0 (window 2 1 0): q = [2, 1, 0] => Output = [2, 2]
        # At 4 (window 1 0 4): q = [4] => Output = [2, 2, 4]
        # At 2 (window 0 4 2): q = [4, 4] => Output = [2, 2, 4, 4]
        # At 6 (window 4 2 6): q = [6] => Output = [2, 2, 4, 4, 6]
        # Solution: Use a deque
        q = deque() # index
        l, r = 0, 0
        res = []
        while r < len(nums):
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)

            if (l > q[0]):
                q.popleft()

            if r + 1 >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1
        return res
