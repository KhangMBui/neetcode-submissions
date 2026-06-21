class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0

        insert_pos = 0

        for n in nums:
            if n != val:
                # Insert to insert_pos:
                nums[insert_pos] = n
                insert_pos += 1
        
        return insert_pos