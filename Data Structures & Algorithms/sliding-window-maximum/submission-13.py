class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # [1, 2, 1, 0, 4, 2, 6], k = 3
        # Idea: use a deque to store index of number in decreasing order
        # so the biggest lies at the front of the queue: [biggest, ...]

        # Also have an output array that adds the biggest number
        # to the queue whenever we reach the appropriate window size
        # and make sure to popleft whenever we exceed our window size

        if not nums or k == 0:
            return []
        q = deque() # Stores decreasing index
        l = r = 0
        output = []
        while r < len(nums):
            # When we meet a number bigger than the biggest in the window
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)

            
            # When reach appropriate window size:
            if r + 1 >= k:
                output.append(nums[q[0]])
                l += 1

            # Remove out of bound left element
            if l > q[0]:
                q.popleft()
            
            r += 1
        return output