class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Solution: Use a deque
        q = deque() # Stores index of nums in decreasing orders
        l, r = 0, 0
        res = []

        while r < len(nums):
            # If the current number is bigger than the
            # front of q, queue it to the front:
            while q and nums[q[-1]] < nums[r]:
                q.pop() # Remove smaller elements from the back
            q.append(r) # Add the current element's index

            # Remove elements outside the current window
            if l > q[0]:
                q.popleft()
            
            # Append the max value when we reach the window size
            if r + 1 >= k:
                res.append(nums[q[0]]) # Front of deque is max value
                l += 1 # Slide the window forward
            r += 1 # Expand the window size
        return res
