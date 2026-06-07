class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Idea: Use a deque to store indexes of decreasing numbers
        # That is, the biggest always in the front of the queue: [biggest, ...]

        # Whenever reached the appropriate size of window k, we add the biggest
        # (front of queue) to the output array. Also check if the window exceed
        # k to remove the leftward out of bound element
        # Repeatedly do this.

        q = deque() # Decreasing index
        l = r = 0
        output = []
        while r < len(nums):
            # When meet a number bigger than the current biggest
            # pop the current biggest and add the new biggest
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)

            # When reached appropriate size of window, add biggest to output:
            if r + 1 >= k:
                output.append(nums[q[0]])
                l += 1
            
            # Check if the leftward out of bound:
            if l > q[0]:
                q.popleft()
            r += 1
        return output