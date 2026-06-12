class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Treat the array like a linked list
        # Use a slow and fast pointer
        slow = fast = 0

        while fast < len(nums):
            slow = nums[slow] # Array version of slow = slow.next
            fast = nums[nums[fast]] # Array version of fast = fast.next.next
            if slow == fast: # cycle detected
                break
        
        slow2 = 0
        while True: # Now move the 2 pointers 1 steps until they meet
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
        