class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # if not nums:
        #     return -1, []
        if not nums:
            return 0
        
        
        # First, count the number of not equal to val and get k
        # [3, 2, 2, 3], val = 3 => k = 2
        # Iterate through nums, ignore val
        # put all number != val to the begin, and set the rest to _

        insert_pos = 0

        for n in nums:
            if n != val:
                # Insert to insert_pos:
                nums[insert_pos] = n
                insert_pos += 1
            # else: # if n == val, we ignore
        
        # After that, we set all elements from insert_pos -> the end '_'
        for i in range(insert_pos, len(nums)):
            nums[i] = '_'
        
        return insert_pos
        # return [insert_pos, nums]